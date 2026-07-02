import random


class ResponseFormatter:

    def __init__(self):

        self.intros = {
            "general": [
                "Gotcha, boss. 😎",
                "On it. 🫡",
                "Easy.",
                "Let's do this.",
                "Say no more.",
                "Alright boss.",
            ],

            "coding": [
                "Time to write some code. 💻",
                "Let's squash this bug. 🐞",
                "Coding mode activated.",
                "Let's build it.",
            ],

            "study": [
                "Let's break it down. 📚",
                "Good question.",
                "Here's the simple explanation.",
            ],

            "success": [
                "Let's goooo! 🚀",
                "Boom! 🎉",
                "Nice work, boss.",
            ],

            "error": [
                "Looks like we found the issue.",
                "No worries, boss.",
                "Let's fix it together.",
            ]
        }

    def format(self, response, mode="general"):

        intro = random.choice(
            self.intros.get(mode, self.intros["general"])
        )

        return f"{intro}\n\n{response}"