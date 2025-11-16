FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

# A small security pump
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose metrics port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8000')" || exit 1


CMD ["python", "main.py"]