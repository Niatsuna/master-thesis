import logging
import time
import torch

from enum import Enum
from transformers import (
  AutoModelForCausalLM,
  AutoModelForSeq2SeqLM,
  AutoTokenizer,
  AutoConfig
)

from metrics import MODEL_LOAD_TIME, INFERENCE_TIME

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
    
  def load(self):
    """Loads model via huggingface and sets modeltype"""
    logger.info(f"Loading model from {self.model_path}")
    start_time = time.time()

    try:
      self.model_type = self.detect_model_type(self.model_path)
      logger.info(f"Model type: {self.model_type.value}")
      self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
      
      # Load appropriate model class
      if self.model_type == ModelType.SEQ2SEQ:
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
          self.config.model_path,
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
      MODEL_LOAD_TIME.observe(load_time)
      logger.info(f"Model loaded successfully in {load_time:.2f} seconds")

    except Exception as e:
      logger.error(f"Failed to load model: {e}")
      raise
  
  def generate(self, prompt: str, max_new_tokens: int = 100):
    """Generate a response for the given prompt"""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    inputs = self.tokenizer(
            prompt,
            return_tensors='pt',
            truncation=True,
            max_length=512
        ).to(device)

    with torch.no_grad():
      start = time.time()
      generation_config = {
        "max_new_tokens": max_new_tokens,
        "pad_token_id": self.tokenizer.eos_token_id
      }
      outputs = self.model.generate(**inputs, **generation_config)

      inference_time = time.time() - start
      INFERENCE_TIME.observe(inference_time)

      input_length = inputs['input_ids'].shape[1]
      generated_tokens = outputs[0, input_length:]
      response = self.tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
      )
      num_tokens = len(generated_tokens)
    
    return response.strip(), inference_time, num_tokens