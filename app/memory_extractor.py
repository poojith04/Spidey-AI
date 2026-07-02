import re


class MemoryExtractor:

    def extract(self, message: str):

        message = message.strip()

        patterns = {

            "name":
                r"my name is (.+)",

            "favorite_language":
                r"my favorite programming language is (.+)",

            "favorite_language":
                r"my favorite language is (.+)",

            "college":
                r"i study at (.+)",

            "goal":
                r"my goal is (.+)",

            "editor":
                r"i use (.+) as my editor"

        }

        lower = message.lower()

        for key, pattern in patterns.items():

            match = re.search(pattern, lower)

            if match:

                return key, match.group(1).strip()

        return None