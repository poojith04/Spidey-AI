from app.brain import Brain
from app.memory import Memory


class Assistant:

    def __init__(self):

        self.brain = Brain()
        self.memory = Memory()

    def chat(self, message):

        self.memory.add("user", message)

        reply = self.brain.think(
            self.memory.get()
        )

        self.memory.add("model", reply)

        return reply