from google import genai
from google.genai import types

from app.config import GEMINI_API_KEY
from app.prompts.system_prompt import SYSTEM_PROMPT


class Brain:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = "gemini-2.5-flash"

    def think(self, history):

        response = self.client.models.generate_content(
            model=self.model,
            contents=history,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )

        return response.text