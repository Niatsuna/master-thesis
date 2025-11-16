import json
import logging
import threading
import time
import psutil

from datetime import datetime, timezone
from confluent_kafka import Consumer, Producer
from concurrent.futures import ThreadPoolExecutor
from prometheus_client import start_http_server

from model import Model
from metrics import ACTIVE_PROCESSING, CPU_USAGE, MEMORY_USAGE, DEVICE_MEMORY, MESSAGES_PROCESSED, TOKENS_GENERATED, PROCESSING_TIME

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
    try:
        process = psutil.Process()
        meminfo = process.memory_info()
        DEVICE_MEMORY.set(float(meminfo.rss))
        MEMORY_USAGE.set(float(psutil.virtual_memory().used))
        CPU_USAGE.set(float(psutil.cpu_percent()))
    except Exception as e:
        logger.warning(f"Failed to update metrics: {e}")
  
  def metrics_worker(self):
    """Small background worker to update metrics without being dependent on main workflow"""
    while self.running:
      self.update_system_metrics()
      time.sleep(10)

  def process_prompt(self, prompt: str, message_id: str):
    start = time.time()
    try:
       response, inference_time, num_tokens = self.model.generate(prompt)
       processing_time = time.time() - start
       PROCESSING_TIME.observe(processing_time)
       TOKENS_GENERATED.inc(num_tokens)

       return {
          'message_id': message_id,
          'prompt': prompt,
          'response': response.strip(),
          'processing_time': processing_time,
          'inference_time': inference_time,
          'tokens_generated': num_tokens,
          'model_type': 'causal_lm',
          'node_id': self.config.node_id,
          'timestamp': datetime.now(timezone.utc).isoformat()
       }
    except Exception as e:
        logger.error(f"Error processing message {message_id}: {e}", exc_info=True)
        return {
            'message_id': message_id,
            'prompt': prompt,
            'error': str(e),
            'model_type': 'causal_lm',
            'node_id': self.config.node_id,
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
  
  def handle_message(self, data):
    message_id = data.get('message_id', 'unknown')
    prompt = data.get('prompt')
    if not prompt:
       return
    ACTIVE_PROCESSING.inc()
    try:
      result = self.process_prompt(prompt, message_id)
      self.producer.produce(
         self.config.output_topic,
         value=json.dumps(result).encode('utf-8')
      )
      self.producer.poll(0)
      MESSAGES_PROCESSED.inc()
    finally:
      ACTIVE_PROCESSING.dec()

  def run(self):
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
          data = json.loads(msg.value().decode('utf-8'))
          self.executor.submit(self.handle_message, data)
    except Exception as e:
       logger.error(f'Service error: {e}', exc_info=True)
    finally:
       self.shutdown()

  def shutdown(self):
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