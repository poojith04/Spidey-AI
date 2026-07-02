from app.brain import Brain
from app.memory_manager import MemoryManager
from app.personality.personality import Personality
from app.formatter import ResponseFormatter
from app.ai_memory import AIMemory
from app.tools.tool_manager import ToolManager
from app.config import USE_AI_MEMORY

class Assistant:

    def __init__(self):

        self.brain = Brain()
        self.memory = MemoryManager()
        self.personality = Personality()
        self.formatter = ResponseFormatter()
        self.extractor = AIMemory()
        self.tools = ToolManager()

    def chat(self, message):

        # ---------------------------------
        # 1. Check Memory
        # ---------------------------------

        stored_answer = self.memory.answer_from_memory(message)

        if stored_answer:
            return self.formatter.format(stored_answer)

        # ---------------------------------
        # 2. Check Tool Commands
        # ---------------------------------

        tool_response = self.tools.execute(message)

        if tool_response:
            return self.formatter.format(tool_response)

        # ---------------------------------
        # 3. AI Memory Extraction
        # ---------------------------------

        if USE_AI_MEMORY and not self.tools.is_tool_command(message):

            memory = self.extractor.extract(message)

            if memory.get("remember"):
                self.memory.remember(
                    memory["key"],
                    memory["value"]
                )

        # ---------------------------------
        # 4. Conversation Memory
        # ---------------------------------

        self.memory.add_message("user", message)

        # ---------------------------------
        # 5. Brain
        # ---------------------------------

        reply = self.brain.think(
            self.memory.get_history()
        )

        self.memory.add_message("model", reply)

        return self.formatter.format(reply)