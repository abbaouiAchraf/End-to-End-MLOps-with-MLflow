from dataclasses import dataclass
from pathlib import Path

# Data classes are to define new variable types with specific attributes
# it can be used to define a return type for a function
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
  root_dir: Path
  unzip_data_dir: Path
  STATUS_FILE: str 
  all_schema: dict
  
@dataclass(frozen=True)
class DataTransformationConfig:
  root_dir: Path
  data_path: Path
  schema: dict