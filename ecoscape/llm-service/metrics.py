from prometheus_client import Counter, Histogram, Gauge

MESSAGES_PROCESSED = Counter('llm_messages_processed_total', 'Total processed messages')
TOKENS_GENERATED = Counter('llm_tokens_generated_total', 'Total tokens generated')

PROCESSING_TIME = Histogram('llm_processing_seconds', 'Time spent processing messages')
MODEL_LOAD_TIME = Histogram('llm_model_load_seconds', 'Time to load the model')
INFERENCE_TIME = Histogram('llm_inference_seconds', 'Time for LLM inference')

ACTIVE_PROCESSING = Gauge('llm_active_processing', 'Number of messages currently being processed')
MEMORY_USAGE = Gauge('llm_memory_usage_bytes', 'Memory usage in bytes')
CPU_USAGE = Gauge('llm_cpu_usage_percent', 'CPU usage percentage')
DEVICE_MEMORY = Gauge('llm_device_memory_bytes', 'Memory usage of compute device (CPU/GPU)')
