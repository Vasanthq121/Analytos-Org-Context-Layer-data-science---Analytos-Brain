from dataclasses import dataclass
from pathlib import Path

@dataclass
class Document:
    file_name: str
    file_path: Path
    content: str