import os
from google import genai
from google.genai import types

try:
    from extractor.prompt import SYSTEM_PROMPT
    from extractor.schema import ExtractionResult
except ModuleNotFoundError:
    from prompt import SYSTEM_PROMPT
    from schema import ExtractionResult


class Extractor:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def extract(self, text: str) -> ExtractionResult:
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                SYSTEM_PROMPT,
                text
            ],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ExtractionResult
            )
        )
        return ExtractionResult.model_validate_json(response.text)
