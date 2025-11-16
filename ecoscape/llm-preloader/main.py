'''
LLM & Dataset Preloader
-----------------------
Downloads llms & datasets from huggingface to '/models/{name}' or '/data/{name}' respectively.
Name is the suffix of the repo id (e.g. 'Qwen/Qwen2.5-0.5B-Instruct' results in 'Qwen2.5-0.5B-Instruct')
'''

import logging
import json
import os
import sys

from datasets import load_dataset
from huggingface_hub import snapshot_download, model_info, dataset_info

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

token = os.environ.get('HF_TOKEN') # Required by models & datasets with gated access (e.g. Llama)
repo_id = os.environ.get('REPO_ID')

i = repo_id.rfind('/')
name = repo_id[i+1:] if i != -1 else repo_id

# Determine type of repo
repo_type = None
try:
  model_info(repo_id)
  repo_type = 'model'
except Exception:
  pass

try:
  dataset_info(repo_id)
  repo_type = 'dataset'
except Exception:
  pass

# Download depending on type
if repo_type == 'model':
  logger.info(f"Repo {repo_id} identified as 'model'. Proceeding with download")
  
  target_dir = f'/models/{name}'
  try:
    snapshot_download(
      repo_id=repo_id,
      local_dir=target_dir,
      use_auth_token=token,
      force_download=True
    )
    logger.info("Download complete!")
  except Exception as e:
    logger.error(f"Failed to process model {name}: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()
    sys.exit

elif repo_type == 'dataset':
  logger.info(f"Repo {repo_id} identified as 'dataset'. Proceeding with download")

  target_dir = f'/data/{name}'
  os.makedirs(target_dir, exist_ok=True)

  try:
    dataset = load_dataset(repo_id)

    for split in dataset.keys():
      dataset[split].to_json(f"{target_dir}/data_{split}.jsonl", orient="records", lines=True, force_ascii=False)
    logger.info(f"Saved data! ({len(dataset.keys())} file(s)!)")

  except Exception as e:
    logger.error(f"Failed to process dataset {name}: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()
    sys.exit
else:
  logger.warning(f"Repo {repo_id} did not identify as either 'model' or 'dataset' but as '{repo_type}'. Abort download")
