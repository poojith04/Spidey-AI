import re


class TaskParser:

    def parse(self, message):

        separators = [
            r"\band\b",
            r"\bthen\b",
            r"\bnext\b",
            r"\balso\b",
            r"\bafter that\b",
            r"\bfinally\b",
            r"\bafterwards\b",
            "&"
        ]

        pattern = "|".join(separators)

        parts = re.split(
            pattern,
            message,
            flags=re.IGNORECASE
        )

        return [
            part.strip()
            for part in parts
            if part.strip()
        ]