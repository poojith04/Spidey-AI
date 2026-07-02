from google import genai
from google.genai import types

from app.config import GEMINI_API_KEY
from app.prompts.system_prompt import SYSTEM_PROMPT


class Brain:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model = "gemini-2.5-flash"

    def think(self, history, context=None):

        contents = []

        # -------------------------
        # Add retrieved knowledge
        # -------------------------

        if context:

            knowledge = """
Answer ONLY using the knowledge below.

If the answer is not present in the knowledge,
say that you couldn't find it in the indexed documents.

Knowledge:
"""

            for item in context:

                knowledge += f"""

Source: {item['source']}

{item['text']}

"""

            contents.append(knowledge)

        # -------------------------
        # Add conversation history
        # -------------------------

        contents.extend(history)

        response = self.client.models.generate_content(

            model=self.model,

            contents=contents,

            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )

        )

        return response.text