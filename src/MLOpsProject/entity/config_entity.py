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
