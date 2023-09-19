import os
from box.exceptions import BoxValueError
import yaml
from MLOpsProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations # decorator for type checking
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory is created at {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at {path}")

@ensure_annotations
def load_json(path: Path):
    with open(path, 'r') as f:
        data = json.load(f)
    logger.info(f"json file loaded from {path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value = data, filename = path)
    logger.info(f"bin file saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(filename = path)
    logger.info(f"bin file loaded from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path) / (1024))
    return f"~ {size_in_kb} KB"