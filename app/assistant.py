from app.brain import Brain
from app.memory_manager import MemoryManager
from app.personality.personality import Personality
from app.formatter import ResponseFormatter
from app.memory_extractor import MemoryExtractor


class Assistant:

    def __init__(self):

        self.brain = Brain()
        self.memory = MemoryManager()
        self.personality = Personality()
        self.formatter = ResponseFormatter()
        self.extractor = MemoryExtractor()

    def chat(self, message):
        memory = self.extractor.extract(message)

        if memory:
            key, value = memory
            self.memory.remember(key, value)
        stored_answer = self.memory.answer_from_memory(message)

        if stored_answer:
            return self.formatter.format(stored_answer)

        self.memory.add_message("user", message)

        reply = self.brain.think(
            self.memory.get_history()
        )

        self.memory.add_message("model", reply)

        return self.formatter.format(reply)