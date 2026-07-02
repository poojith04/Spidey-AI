import json

from google import genai
from google.genai import types

from app.config import GEMINI_API_KEY


class AIMemory:

    def __init__(self):

        self.client = genai.Client(api_key=GEMINI_API_KEY)

        self.model = "gemini-2.5-flash"

    def extract(self, message):

        prompt = f"""
You are an AI memory extraction engine.

Read the user's message.

Determine whether it contains long-term personal information worth remembering.

Examples:

"My name is John."

"My favorite language is Python."

"I study at SRGEC."

"I'm learning Kubernetes."

"My goal is to become an AI Engineer."

Ignore:

Greetings

Questions

Casual conversation

Return ONLY JSON.

Example:

{{
    "remember": true,
    "key": "favorite_language",
    "value": "Python"
}}

or

{{
    "remember": false
}}

Message:

{message}
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0
            )
        )

        try:

            return json.loads(response.text)

        except Exception:

            return {
                "remember": False
            }