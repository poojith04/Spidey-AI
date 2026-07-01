from google import genai
from app.config import GEMINI_API_KEY


class Brain:

    def __init__(self):

        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = "gemini-2.5-flash"

    def think(self, history):

        response = self.client.models.generate_content(
            model=self.model,
            contents=history
        )

        return response.text