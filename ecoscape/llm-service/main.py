import logging
from config import Config
from service import LLMService

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

if __name__ == '__main__':
  config = Config.from_env()
  service = LLMService(config)
  service.run()