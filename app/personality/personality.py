import random


class Personality:

    def __init__(self):

        self.greetings = [
            "Yo boss! 😎",
            "Hey chief! What's on today's mission?",
            "Back again? Nice 😄",
            "What's up, boss?",
            "Ready to build something awesome today? 🚀",
            "Good to see you again, boss.",
            "Let's make something cool today.",
            "Alright boss, I'm all ears.",
            "Mission control online. 😎",
            "Hey partner! What's the plan?"
        ]

        self.acknowledgements = [
            "On it. 🫡",
            "Got it, boss.",
            "Easy.",
            "Say no more.",
            "I'm on it.",
            "Let's do it.",
            "Sounds good.",
            "Consider it done.",
            "Gotcha.",
            "Absolutely."
        ]

        self.success = [
            "Boom! 🎉",
            "Let's goooo! 🚀",
            "Mission accomplished.",
            "Nice work, boss!",
            "That turned out great!",
            "We nailed it.",
            "Smooth. 😎",
            "Another win!",
            "That worked perfectly.",
            "Success!"
        ]

        self.errors = [
            "Hmm... looks like we hit a small bump.",
            "Interesting... let's figure this out.",
            "No worries, boss. We'll fix it.",
            "That didn't go as planned.",
            "Looks like something needs our attention.",
            "Let's debug this together.",
            "Small issue. Nothing we can't handle.",
            "Let's investigate."
        ]

    def greeting(self):
        return random.choice(self.greetings)

    def acknowledgement(self):
        return random.choice(self.acknowledgements)

    def success_message(self):
        return random.choice(self.success)

    def error_message(self):
        return random.choice(self.errors)
