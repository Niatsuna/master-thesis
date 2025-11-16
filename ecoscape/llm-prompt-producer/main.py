import os
import json
import time
import random
import logging
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum
import numpy as np

from prometheus_client import Counter, Gauge, Histogram, Summary, start_http_server
from confluent_kafka import Producer
from confluent_kafka import KafkaException


# Configuration
class LoadPattern(Enum):
    CONSTANT = "constant"
    POISSON = "poisson"
    BURST = "burst"
    RAMP_UP = "ramp_up"


@dataclass
class ProducerConfig:
    # Kafka settings
    kafka_bootstrap_servers: str
    kafka_topic: str
    
    # Dataset settings
    dataset_path: str
    
    # Load generation settings
    load_pattern: LoadPattern = LoadPattern.POISSON
    base_rps: float = 10.0          # Requests per second
    duration_seconds: int = 300     # Total duration
    burst_size: int = 100           # For burst pattern
    burst_interval: int = 60        # Seconds between bursts
    ramp_up_end_rps: float = 50.0   # For ramp_up pattern
    
    # Prompt filtering
    min_prompt_length: int = 10   # tokens
    max_prompt_length: int = 500  # tokens
    
    # Length distribution (should sum to 1.0)
    short_prompts_ratio: float = 0.4    # 10-50 tokens
    medium_prompts_ratio: float = 0.4   # 50-200 tokens
    long_prompts_ratio: float = 0.2     # 200-500 tokens

    metrics_port: int = 5000

# Prometheus metrics
PROMPTS_SENT_TOTAL = Counter(
    'prompts_sent_total',
    'Total number of prompts sent to Kafka',
    ['load_pattern', 'prompt_length_category']
)

PROMPTS_ERRORS_TOTAL = Counter(
    'prompts_errors_total',
    'Total number of errors sending prompts',
    ['load_pattern', 'error_type']
)

PROMPTS_IN_FLIGHT = Gauge(
    'prompts_in_flight',
    'Number of prompts currently being processed',
    ['load_pattern']
)

PROMPT_SEND_DURATION = Histogram(
    'prompt_send_duration_seconds',
    'Time taken to send prompt to Kafka',
    ['load_pattern'],
    buckets=[0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0]
)

PROMPT_TOKEN_COUNT = Histogram(
    'prompt_token_count',
    'Distribution of prompt token counts',
    ['prompt_length_category'],
    buckets=[10, 25, 50, 100, 150, 200, 300, 400, 500]
)

CURRENT_RPS = Gauge(
    'current_requests_per_second',
    'Current requests per second rate',
    ['load_pattern']
)

KAFKA_LAG = Gauge(
    'kafka_producer_lag_seconds',
    'Estimated lag between send and ack',
    ['load_pattern']
)

class PromptDataset:
    """Handles loading and categorizing prompts from LMSYS-Chat-1M"""
    
    def __init__(self, dataset_path: str, config: ProducerConfig):
        self.dataset_path = Path(dataset_path)
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        self.short_prompts: List[Dict] = []
        self.medium_prompts: List[Dict] = []
        self.long_prompts: List[Dict] = []
        
        self._load_dataset()
    
    def _estimate_tokens(self, text: str) -> int:
        """Rough token estimation (1 token ≈ 4 chars for English)"""
        return len(text) // 4
    
    def _load_dataset(self):
      """Load and categorize prompts by length"""
      self.logger.info(f"Loading dataset from {self.dataset_path}")
      
      if not self.dataset_path.exists():
          raise FileNotFoundError(f"Dataset not found at {self.dataset_path}")
      
      loaded_count = 0
      
      with open(self.dataset_path, 'r', encoding='utf-8') as f:
          for line in f:
              try:
                  data = json.loads(line.strip())
                  
                  if data["input"].strip():
                      prompt = f"Instruction: {data["instruction"]}\nInput: {data['input']}"
                  else:
                      prompt = f"Instruction: {data["instruction"]}"
                  
                  # Estimate token count
                  token_count = self._estimate_tokens(prompt)
                  
                  # Filter by length
                  if token_count < self.config.min_prompt_length:
                      continue
                  if token_count > self.config.max_prompt_length:
                      continue
                  
                  # Categorize by length
                  prompt_data = {
                      'text': prompt,
                      'token_count': token_count,
                      'original_id': data.get('id', loaded_count)
                  }
                  
                  if token_count <= 50:
                      self.short_prompts.append(prompt_data)
                  elif token_count <= 200:
                      self.medium_prompts.append(prompt_data)
                  else:
                      self.long_prompts.append(prompt_data)
                  
                  loaded_count += 1
                  
                  # Progress logging
                  if loaded_count % 10000 == 0:
                      self.logger.info(f"Loaded {loaded_count} prompts...")
              
              except json.JSONDecodeError:
                  continue
              except Exception as e:
                  self.logger.warning(f"Error processing line: {e}")
                  continue
      
      self.logger.info(f"Dataset loaded: {len(self.short_prompts)} short, "
                      f"{len(self.medium_prompts)} medium, "
                      f"{len(self.long_prompts)} long prompts")
      
      if loaded_count == 0:
          raise ValueError("No prompts loaded from dataset!")
    
    def sample_prompt(self) -> Dict:
      """Sample a prompt based on configured length distribution"""
      rand = random.random()
      
      if rand < self.config.short_prompts_ratio:
          prompt = random.choice(self.short_prompts)
          category = 'short'
      elif rand < self.config.short_prompts_ratio + self.config.medium_prompts_ratio:
          prompt = random.choice(self.medium_prompts)
          category = 'medium'
      else:
          prompt = random.choice(self.long_prompts)
          category = 'long'
      
      # Record token count distribution
      PROMPT_TOKEN_COUNT.labels(prompt_length_category=category).observe(prompt['token_count'])
      
      prompt['length_category'] = category  # Add category to prompt data
      return prompt


class LoadGenerator:
    """Generates inter-arrival times based on load pattern"""
    
    def __init__(self, config: ProducerConfig):
        self.config = config
        self.start_time = time.time()
        self.request_count = 0
        self.logger = logging.getLogger(__name__)
    
    def get_next_delay(self) -> float:
        """Calculate delay until next request based on pattern"""
        
        if self.config.load_pattern == LoadPattern.CONSTANT:
            return 1.0 / self.config.base_rps
        
        elif self.config.load_pattern == LoadPattern.POISSON:
            # Poisson process: exponential inter-arrival times
            return np.random.exponential(1.0 / self.config.base_rps)
        
        elif self.config.load_pattern == LoadPattern.BURST:
            # Send burst_size requests quickly, then wait
            if self.request_count % self.config.burst_size == 0:
                self.logger.info(f"Starting burst at request {self.request_count}")
                return self.config.burst_interval
            else:
                return 0.1  # Fast sending within burst
        
        elif self.config.load_pattern == LoadPattern.RAMP_UP:
            # Linear ramp from base_rps to ramp_up_end_rps
            elapsed = time.time() - self.start_time
            progress = min(elapsed / self.config.duration_seconds, 1.0)
            
            current_rps = (self.config.base_rps + 
                          (self.config.ramp_up_end_rps - self.config.base_rps) * progress)
            
            return 1.0 / current_rps
        
        return 1.0 / self.config.base_rps


class PromptProducer:
    """Main producer class that sends prompts to Kafka"""
    
    def __init__(self, config: ProducerConfig):
        self.config = config
        self.logger = self._setup_logging()
        
        self.dataset = PromptDataset(config.dataset_path, config)
        self.load_generator = LoadGenerator(config)
        
        self.producer = self._create_kafka_producer()
        
        # Statistics
        self.sent_count = 0
        self.error_count = 0
        self.start_time = None
    
    def _setup_logging(self) -> logging.Logger:
        """Configure logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger(__name__)
    
    def _create_kafka_producer(self) -> Producer:
      """Create Kafka producer with retry logic"""
      self.logger.info(f"Connecting to Kafka at {self.config.kafka_bootstrap_servers}")
      
      conf = {
          'bootstrap.servers': self.config.kafka_bootstrap_servers,
          'compression.type': 'gzip',
          'acks': 'all',
          'retries': 3,
          'linger.ms': 10,
      }
    
      return Producer(conf)
    
    def _on_send_success(self, err, msg):
      """Callback for successful sends"""
      if err is not None:
          self.error_count += 1
          error_type = type(err).__name__
          PROMPTS_ERRORS_TOTAL.labels(
              load_pattern=self.config.load_pattern.value,
              error_type=error_type
          ).inc()
          self.logger.error(f"Error sending prompt: {err}")
          return
      
      self.sent_count += 1
      
      # Decrement in-flight counter
      PROMPTS_IN_FLIGHT.labels(load_pattern=self.config.load_pattern.value).dec()
      
      # Calculate and record lag
      if hasattr(self, '_last_send_time'):
          lag = time.time() - self._last_send_time
          KAFKA_LAG.labels(load_pattern=self.config.load_pattern.value).set(lag)
      
      if self.sent_count % 100 == 0:
          elapsed = time.time() - self.start_time
          rps = self.sent_count / elapsed
          CURRENT_RPS.labels(load_pattern=self.config.load_pattern.value).set(rps)
          self.logger.info(f"Sent {self.sent_count} prompts "
                        f"({rps:.2f} RPS, {self.error_count} errors)")
    
    def _on_send_error(self, exc):
        """Callback for send errors"""
        self.error_count += 1
        self.logger.error(f"Error sending prompt: {exc}")
    
    def send_prompt(self, prompt_data: Dict) -> bool:
      """Send a single prompt to Kafka"""
      message = {
          'message_id': f"{self.sent_count}_{int(time.time() * 1000)}",
          'prompt': prompt_data['text'],
          'token_count': prompt_data['token_count'],
          'timestamp': time.time(),
          'metadata': {
              'original_id': prompt_data['original_id'],
              'load_pattern': self.config.load_pattern.value,
              'request_number': self.sent_count
          }
      }
      
      # Increment in-flight counter
      PROMPTS_IN_FLIGHT.labels(load_pattern=self.config.load_pattern.value).inc()
      
      send_start = time.time()
      self._last_send_time = send_start
      
      try:
          self.producer.produce(
              self.config.kafka_topic,
              value=json.dumps(message).encode('utf-8'),
              callback=self._on_send_success
          )
          self.producer.poll(0)
          
          duration = time.time() - send_start
          PROMPT_SEND_DURATION.labels(load_pattern=self.config.load_pattern.value).observe(duration)
          
          PROMPTS_SENT_TOTAL.labels(
              load_pattern=self.config.load_pattern.value,
              prompt_length_category=prompt_data.get('length_category', 'unknown')
          ).inc()
          
          return True
      
      except KafkaException as e:
          # Decrement in-flight on immediate error
          PROMPTS_IN_FLIGHT.labels(load_pattern=self.config.load_pattern.value).dec()
          
          error_type = type(e).__name__
          PROMPTS_ERRORS_TOTAL.labels(
              load_pattern=self.config.load_pattern.value,
              error_type=error_type
          ).inc()
          
          self.logger.error(f"Kafka error: {e}")
          self.error_count += 1
          return False
    
    def run(self):
      """Main execution loop"""
      # Start Prometheus metrics server
      try:
          start_http_server(self.config.metrics_port)
          self.logger.info(f"Prometheus metrics server started on port {self.config.metrics_port}")
      except Exception as e:
          self.logger.warning(f"Failed to start metrics server: {e}")
      
      self.logger.info(f"Starting prompt producer")
      self.logger.info(f"Load pattern: {self.config.load_pattern.value}")
      self.logger.info(f"Starting prompt producer")
      self.logger.info(f"Load pattern: {self.config.load_pattern.value}")
      self.logger.info(f"Target RPS: {self.config.base_rps}")
      self.logger.info(f"Duration: {self.config.duration_seconds}s")
      
      self.start_time = time.time()
      self.load_generator.start_time = self.start_time
      
      try:
          while True:
              elapsed = time.time() - self.start_time
              if elapsed >= self.config.duration_seconds:
                  self.logger.info("Duration reached, stopping...")
                  break

              prompt_data = self.dataset.sample_prompt()
              self.send_prompt(prompt_data)

              self.load_generator.request_count += 1

              delay = self.load_generator.get_next_delay()
              time.sleep(max(0, delay))
      
      except KeyboardInterrupt:
          self.logger.info("Received interrupt signal, stopping...")
      
      finally:
          self._shutdown()
    
    def _shutdown(self):
        """Clean shutdown"""
        self.logger.info("Flushing remaining messages...")
        self.producer.flush(timeout=10)
        
        # Final statistics
        elapsed = time.time() - self.start_time
        avg_rps = self.sent_count / elapsed if elapsed > 0 else 0
        
        self.logger.info("=" * 50)
        self.logger.info(f"Producer stopped")
        self.logger.info(f"Total prompts sent: {self.sent_count}")
        self.logger.info(f"Total errors: {self.error_count}")
        self.logger.info(f"Duration: {elapsed:.2f}s")
        self.logger.info(f"Average RPS: {avg_rps:.2f}")
        self.logger.info("=" * 50)


def main():
    config = ProducerConfig(
      kafka_bootstrap_servers=os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
      kafka_topic=os.getenv('KAFKA_TOPIC'),
      dataset_path=os.getenv('DATASET_PATH'),
      load_pattern=LoadPattern(os.getenv('LOAD_PATTERN', 'poisson')),
      base_rps=float(os.getenv('BASE_RPS', '10.0')),
      duration_seconds=int(os.getenv('DURATION_SECONDS', '300')),
      burst_size=int(os.getenv('BURST_SIZE', '100')),
      burst_interval=int(os.getenv('BURST_INTERVAL', '60')),
      ramp_up_end_rps=float(os.getenv('RAMP_UP_END_RPS', '50.0')),
    )
    
    producer = PromptProducer(config)
    producer.run()


if __name__ == "__main__":
    main()