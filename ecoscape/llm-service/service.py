import json
import logging
import threading
import time
import psutil
import sys

from datetime import datetime, timezone
from confluent_kafka import Consumer, Producer
from concurrent.futures import ThreadPoolExecutor
from prometheus_client import start_http_server

from model import Model
from metrics import (
    ACTIVE_PROCESSING,
    CPU_USAGE,
    MEMORY_USAGE,
    DEVICE_MEMORY,
    MESSAGES_PROCESSED,
    TOKENS_GENERATED,
    PROCESSING_TIME,
    REQUESTS_SUCCESS,
    REQUESTS_FAILED,
    QUEUE_DEPTH,
    TOKENS_PER_SECOND,
    get_labels
)

logger = logging.getLogger(__name__)

class LLMService:
  def __init__(self, config):
    self.config = config
    self.model = Model(config.model_path)
    self.consumer = None
    self.producer = None
    self.running = False
    self.metrics_thread = None
    self.executor = ThreadPoolExecutor(max_workers=2)
    self._token_count_window = []
    self._token_window_size = 10

  def setup_kafka(self):
    """Setup basic kafka consumer and producer"""
    try:
        self.consumer = Consumer({
            'bootstrap.servers': self.config.kafka_bootstrap_servers,
            'group.id': self.config.consumer_group,
            'auto.offset.reset': 'latest',
        })
        self.consumer.subscribe([self.config.input_topic])
        
        self.producer = Producer({
            'bootstrap.servers': self.config.kafka_bootstrap_servers
        })
        logger.info("Kafka setup complete")
    except Exception as e:
        logger.error(f"Failed to setup kafka: {e}")
        raise
  
  def update_system_metrics(self):
    """Update system resource metrics"""
    try:
        labels = get_labels()
        process = psutil.Process()
        meminfo = process.memory_info()
        
        DEVICE_MEMORY.labels(**labels).set(float(meminfo.rss))
        MEMORY_USAGE.labels(**labels).set(float(psutil.virtual_memory().used))
        CPU_USAGE.labels(**labels).set(float(psutil.cpu_percent()))
        
        # Calculate tokens per second
        current_time = time.time()
        self._token_count_window = [
            (t, count) for t, count in self._token_count_window 
            if current_time - t < self._token_window_size
        ]
        
        if self._token_count_window:
            total_tokens = sum(count for _, count in self._token_count_window)
            time_span = current_time - self._token_count_window[0][0]
            if time_span > 0:
                tps = total_tokens / time_span
                TOKENS_PER_SECOND.labels(**labels).set(tps)
        
    except Exception as e:
        logger.warning(f"Failed to update metrics: {e}")
  
  def metrics_worker(self):
    """Background worker to update metrics"""
    while self.running:
      self.update_system_metrics()
      time.sleep(10)

  def process_prompt(self, prompt: str, message_id: str):
    """Process a prompt and track metrics"""
    labels = get_labels()
    start = time.time()
    
    try:
       response, inference_time, num_tokens, input_length = self.model.generate(prompt)
       processing_time = time.time() - start
       
       PROCESSING_TIME.labels(**labels).observe(processing_time)
       TOKENS_GENERATED.labels(**labels).inc(num_tokens)
       REQUESTS_SUCCESS.labels(**labels).inc()
       
       self._token_count_window.append((time.time(), num_tokens))
       
       return {
          'message_id': message_id,
          'prompt': prompt,
          'response': response.strip(),
          'processing_time': processing_time,
          'inference_time': inference_time,
          'tokens_generated': num_tokens,
          'input_tokens': input_length,
          'model_type': self.model.model_type.value if self.model.model_type else 'unknown',
          'node_id': self.config.node_id,
          'timestamp': datetime.now(timezone.utc).isoformat(),
          'status': 'success'
       }
       
    except Exception as e:
        logger.error(f"Error processing message {message_id}: {e}", exc_info=True)
        error_reason = type(e).__name__
        REQUESTS_FAILED.labels(**labels, reason=error_reason).inc()
        
        return {
            'message_id': message_id,
            'prompt': prompt,
            'error': str(e),
            'error_type': error_reason,
            'node_id': self.config.node_id,
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'status': 'failed'
        }
  
  def handle_message(self, data):
    """Handle incoming Kafka message"""
    labels = get_labels()
    message_id = data.get('message_id', 'unknown')
    prompt = data.get('prompt')
    
    if not prompt:
       logger.warning(f"Message {message_id} has no prompt")
       REQUESTS_FAILED.labels(**labels, reason='no_prompt').inc()
       return
    
    ACTIVE_PROCESSING.labels(**labels).inc()
    
    try:
      result = self.process_prompt(prompt, message_id)
      
      self.producer.produce(
         self.config.output_topic,
         value=json.dumps(result).encode('utf-8')
      )
      self.producer.poll(0)
      
      status = result.get('status', 'success')
      MESSAGES_PROCESSED.labels(**labels, status=status).inc()
      
    except Exception as e:
      logger.error(f"Failed to handle message {message_id}: {e}")
      REQUESTS_FAILED.labels(**labels, reason='handling_error').inc()
      
    finally:
      ACTIVE_PROCESSING.labels(**labels).dec()

  def update_queue_depth(self):
    """Update queue depth metric"""
    try:
      labels = get_labels()
      queue_size = self.executor._work_queue.qsize()
      QUEUE_DEPTH.labels(**labels).set(queue_size)
    except Exception as e:
      logger.debug(f"Could not update queue depth: {e}")

  def run(self):
    """Main service loop"""
    logger.info(f"Starting LLM Service on node {self.config.node_id}")
    start_http_server(self.config.metrics_port)

    self.model.load()
    self.setup_kafka()

    self.running = True
    self.metrics_thread = threading.Thread(target=self.metrics_worker, daemon=True)
    self.metrics_thread.start()

    logger.info("LLM Service ready")
    
    try:
       while self.running:
          msg = self.consumer.poll(timeout=0.1)
          
          if msg is None or msg.error():
             continue
          
          try:
            data = json.loads(msg.value().decode('utf-8'))
            self.executor.submit(self.handle_message, data)
            self.update_queue_depth()
            
          except json.JSONDecodeError as e:
            logger.error(f"Failed to decode message: {e}")
            labels = get_labels()
            REQUESTS_FAILED.labels(**labels, reason='json_decode_error').inc()
            
    except KeyboardInterrupt:
       logger.info("Received shutdown signal")
    except Exception as e:
       logger.error(f'Service error: {e}', exc_info=True)
    finally:
       self.shutdown()

  def shutdown(self):
     """Clean shutdown"""
     logger.info('Shutting down...')
     self.running = False
     if self.metrics_thread:
        self.metrics_thread.join(timeout=2)
     if self.consumer:
        self.consumer.close()
     if self.producer:
        self.producer.flush()
     self.executor.shutdown(wait=True)
     logger.info("Shutdown complete!")