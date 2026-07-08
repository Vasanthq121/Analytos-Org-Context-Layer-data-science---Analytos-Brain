from pathlib import Path
from .parser import MarkdownParser


class DocumentLoader:

    def __init__(self):

        self.parser = MarkdownParser()

    def load_documents(self, folder):

        folder = Path(folder)

        docs = []

        for file in folder.glob("*.md"):

            docs.append(self.parser.parse(file))

        return docs