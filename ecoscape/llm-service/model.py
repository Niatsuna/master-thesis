import logging
import time
import torch
from threading import Thread

from enum import Enum
from transformers import (
  AutoModelForCausalLM,
  AutoModelForSeq2SeqLM,
  AutoTokenizer,
  AutoConfig,
  TextIteratorStreamer
)

from metrics import (
    MODEL_LOAD_TIME, 
    INFERENCE_TIME, 
    TTFT,
    INTER_TOKEN_LATENCY,
    INPUT_TOKENS,
    GPU_UTILIZATION,
    GPU_MEMORY_USAGE,
    get_labels
)

logger = logging.getLogger(__name__)

class ModelType(Enum):
  CAUSAL_LM = "causal"
  SEQ2SEQ = "seq2seq"

class Model:
  def __init__(self, model_path: str):
    self.model_path = model_path
    self.model = None
    self.tokenizer = None
    self.model_type = None

  def detect_model_type(self, model_path: str) -> ModelType:
    """Detect if model is Causal LM or Seq2Seq"""
    try:
      config = AutoConfig.from_pretrained(model_path)
      
      architectures = getattr(config, 'architectures', [])
      if architectures:
        arch_str = str(architectures[0]).lower()
          
        # Seq2Seq indicators
        if any(x in arch_str for x in ['seq2seq', 't5', 'bart', 'pegasus', 'mbart']):
          logger.info(f"Detected Seq2Seq model: {architectures[0]}")
          return ModelType.SEQ2SEQ
        
        # Causal LM indicators
        if any(x in arch_str for x in ['causallm', 'gpt', 'llama', 'opt', 'bloom']):
          logger.info(f"Detected Causal LM model: {architectures[0]}")
          return ModelType.CAUSAL_LM
      
      if hasattr(config, 'is_encoder_decoder') and config.is_encoder_decoder:
        logger.info("Detected Seq2Seq model via is_encoder_decoder flag")
        return ModelType.SEQ2SEQ
      else:
        logger.info("Detected Causal LM model (no encoder)")
        return ModelType.CAUSAL_LM
            
    except Exception as e:
      logger.warning(f"Could not auto-detect model type: {e}. Defaulting to Causal LM")
      return ModelType.CAUSAL_LM
  
  def update_gpu_metrics(self):
    """Update GPU metrics if GPU is available"""
    if torch.cuda.is_available():
      try:
        import pynvml
        if not hasattr(self, '_nvml_initialized'):
          pynvml.nvmlInit()
          self._nvml_initialized = True
          self._nvml_handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        
        labels = get_labels()
        util = pynvml.nvmlDeviceGetUtilizationRates(self._nvml_handle)
        GPU_UTILIZATION.labels(**labels).set(float(util.gpu))
        
        mem_info = pynvml.nvmlDeviceGetMemoryInfo(self._nvml_handle)
        GPU_MEMORY_USAGE.labels(**labels).set(float(mem_info.used))
      except Exception as e:
        logger.debug(f"Could not update GPU metrics: {e}")
    
  def load(self):
    """Loads model via huggingface and sets modeltype"""
    logger.info(f"Loading model from {self.model_path}")
    start_time = time.time()

    try:
      self.model_type = self.detect_model_type(self.model_path)
      logger.info(f"Model type: {self.model_type.value}")
      self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
      
      if self.model_type == ModelType.SEQ2SEQ:
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
          self.model_path,
          torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
          device_map="auto" if torch.cuda.is_available() else None,
          low_cpu_mem_usage=True
        )
      else:
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        
        self.model = AutoModelForCausalLM.from_pretrained(
          self.model_path,
          torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
          device_map="auto" if torch.cuda.is_available() else None,
          low_cpu_mem_usage=True
        )

      load_time = time.time() - start_time
      labels = get_labels()
      MODEL_LOAD_TIME.labels(**labels).observe(load_time)
      logger.info(f"Model loaded successfully in {load_time:.2f} seconds")

    except Exception as e:
      logger.error(f"Failed to load model: {e}")
      raise
  
  def generate(self, prompt: str, max_new_tokens: int = 100):
    """
    Generate response with ACCURATE TTFT and ITL using streaming.
    
    This implementation uses TextIteratorStreamer to capture precise timing
    for each token as it's generated, providing accurate TTFT and ITL measurements.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    labels = get_labels()
    
    # Tokenize input
    inputs = self.tokenizer(
            prompt,
            return_tensors='pt',
            truncation=True,
            max_length=512
        ).to(device)

    input_length = inputs['input_ids'].shape[1]
    INPUT_TOKENS.labels(**labels).inc(input_length)

    # Setup streaming
    streamer = TextIteratorStreamer(
        self.tokenizer,
        skip_prompt=True,  # Don't return the prompt in output
        skip_special_tokens=True
    )
    
    generation_config = {
        "max_new_tokens": max_new_tokens,
        "pad_token_id": self.tokenizer.eos_token_id,
        "streamer": streamer
    }
    
    # Merge inputs and generation config
    generation_kwargs = {**inputs, **generation_config}
    
    # Start generation in separate thread
    inference_start = time.time()
    thread = Thread(target=self.model.generate, kwargs=generation_kwargs)
    thread.start()
    
    # Track token generation timing
    first_token_time = None
    last_token_time = inference_start
    response_parts = []
    token_count = 0
    
    try:
        for text_chunk in streamer:
            current_time = time.time()
            
            if first_token_time is None:
                # First token received - record TTFT
                first_token_time = current_time
                ttft = first_token_time - inference_start
                TTFT.labels(**labels).observe(ttft)
                logger.debug(f"TTFT: {ttft:.3f}s")
            else:
                # Subsequent tokens - record ITL
                itl = current_time - last_token_time
                INTER_TOKEN_LATENCY.labels(**labels).observe(itl)
            
            last_token_time = current_time
            response_parts.append(text_chunk)
            token_count += 1
    
    except Exception as e:
        logger.error(f"Error during streaming generation: {e}")
        raise
    finally:
        thread.join()
    
    inference_time = time.time() - inference_start
    INFERENCE_TIME.labels(**labels).observe(inference_time)
    
    # Combine response
    response = ''.join(response_parts)
    
    # Update GPU metrics
    self.update_gpu_metrics()
    
    return response.strip(), inference_time, token_count, input_length