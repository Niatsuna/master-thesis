import os

from dataclasses import dataclass

@dataclass
class Config:
  kafka_bootstrap_servers : str
  input_topic : str
  output_topic : str

  model_path: str
  node_id: str

  max_new_tokens: int = 256
  temperature: float = 0.7
  do_sample: bool = True
  metrics_port: int = 8000
  consumer_group : str = None
  device_type: str = "auto"  # can be "cpu", "cuda", or "auto"

  @classmethod
  def from_env(cls) -> 'Config':
    node_id = os.getenv('NODE_ID')
    device_type = os.getenv('DEVICE_TYPE', 'auto')
    return cls(
      kafka_bootstrap_servers = os.getenv('BOOTSTRAP_SERVER'),
      input_topic = os.getenv('INPUT_TOPIC'),
      output_topic = os.getenv('OUTPUT_TOPIC'),
      model_path = os.getenv('MODEL_PATH'),
      node_id = node_id,
      max_new_tokens = int(os.getenv('MAX_NEW_TOKENS', '256')),
      temperature = float(os.getenv('TEMPERATURE', '0.7')),
      do_sample = os.getenv('DO_SAMPLE', 'true').lower() == 'true',
      metrics_port = int(os.getenv('METRICS_PORT', '8000')),
      consumer_group = os.getenv('CONSUMER_GROUP', node_id),
      device_type=device_type
      )