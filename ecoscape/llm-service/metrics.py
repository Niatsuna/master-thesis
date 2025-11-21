import os
from prometheus_client import Counter, Histogram, Gauge

NODE_ID = os.getenv('NODE_ID', 'default')
NODE_TYPE = os.getenv('NODE_TYPE', 'edge')  # edge, cloud, fog
DEVICE_TYPE = os.getenv('DEVICE_TYPE', 'cpu')  # cpu, gpu

MESSAGES_PROCESSED = Counter(
    'llm_messages_processed_total',
    'Total processed messages',
    ['node_id', 'node_type', 'device_type', 'status']
)

INPUT_TOKENS = Counter(
    'llm_input_tokens_total',
    'Total input tokens processed',
    ['node_id', 'node_type', 'device_type']
)

INTER_TOKEN_LATENCY = Histogram(
    'llm_inter_token_latency_seconds',
    'Time between consecutive tokens',
    ['node_id', 'node_type', 'device_type'],
    buckets=[0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]
)

TOKENS_GENERATED = Counter(
    'llm_tokens_generated_total',
    'Total output tokens generated',
    ['node_id', 'node_type', 'device_type']
)

TTFT = Histogram(
    'llm_time_to_first_token_seconds',
    'Time from request start to first token generated',
    ['node_id', 'node_type', 'device_type'],
    buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0]
)

PROCESSING_TIME = Histogram(
    'llm_processing_seconds',
    'Complete time spent processing messages',
    ['node_id', 'node_type', 'device_type'],
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 30.0, 60.0, 120.0]
)

REQUESTS_SUCCESS = Counter(
    'llm_requests_success_total',
    'Successfully completed requests',
    ['node_id', 'node_type', 'device_type']
)

REQUESTS_FAILED = Counter(
    'llm_requests_failed_total',
    'Failed requests',
    ['node_id', 'node_type', 'device_type', 'reason']
)

INFERENCE_TIME = Histogram(
    'llm_inference_seconds',
    'Time for LLM inference only',
    ['node_id', 'node_type', 'device_type'],
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 30.0, 60.0]
)

MODEL_LOAD_TIME = Histogram(
    'llm_model_load_seconds',
    'Time to load the model',
    ['node_id', 'node_type', 'device_type'],
    buckets=[1.0, 5.0, 10.0, 30.0, 60.0, 120.0, 300.0]
)

ACTIVE_PROCESSING = Gauge(
    'llm_active_processing',
    'Number of messages currently being processed',
    ['node_id', 'node_type', 'device_type']
)

QUEUE_DEPTH = Gauge(
    'llm_request_queue_depth',
    'Number of requests waiting in queue',
    ['node_id', 'node_type', 'device_type']
)

TOKENS_PER_SECOND = Gauge(
    'llm_tokens_per_second',
    'Current token generation rate',
    ['node_id', 'node_type', 'device_type']
)

MEMORY_USAGE = Gauge(
    'llm_memory_usage_bytes',
    'System memory usage',
    ['node_id', 'node_type', 'device_type']
)

CPU_USAGE = Gauge(
    'llm_cpu_usage_percent',
    'CPU usage percentage',
    ['node_id', 'node_type', 'device_type']
)

DEVICE_MEMORY = Gauge(
    'llm_device_memory_bytes',
    'Process memory usage',
    ['node_id', 'node_type', 'device_type']
)

GPU_UTILIZATION = Gauge(
    'llm_gpu_utilization_percent',
    'GPU utilization percentage',
    ['node_id', 'node_type', 'device_type']
)

GPU_MEMORY_USAGE = Gauge(
    'llm_gpu_memory_bytes',
    'GPU memory usage',
    ['node_id', 'node_type', 'device_type']
)

def get_labels():
    """Get standard metric labels from environment variables"""
    return {
        'node_id': NODE_ID,
        'node_type': NODE_TYPE,
        'device_type': DEVICE_TYPE
    }