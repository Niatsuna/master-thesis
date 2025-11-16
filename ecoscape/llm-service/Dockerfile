FROM nvidia/cuda:12.1.0-base-ubuntu22.04 AS base

RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Builder stage
FROM base AS builder

ARG COMPUTE_TYPE=cpu

# Install PyTorch based on compute type
RUN if [ "$COMPUTE_TYPE" = "gpu" ]; then \
        pip3 install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121; \
    else \
        pip3 install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu; \
    fi

RUN pip3 install --no-cache-dir transformers accelerate \
    confluent_kafka prometheus-client psutil requests

# Runtime stage
FROM base AS runtime

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/dist-packages /usr/local/lib/python3.10/dist-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . .

RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD python3 -c "import requests; requests.get('http://localhost:8000')" || exit 1

CMD ["python3", "main.py"]