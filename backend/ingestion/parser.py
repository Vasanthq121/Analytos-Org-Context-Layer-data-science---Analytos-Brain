from pathlib import Path
from .models import Document


class MarkdownParser:

    def parse(self, file_path: Path) -> Document:

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        return Document(
            file_name=file_path.name,
            file_path=file_path,
            content=text
        )