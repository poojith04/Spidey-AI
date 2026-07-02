from app.core.brain import Brain
from app.memory.memory_manager import MemoryManager
from app.personality.personality import Personality
from app.formatting.formatter import ResponseFormatter
from database.ai_memory import AIMemory
from app.tools.tool_manager import ToolManager
from app.config import USE_AI_MEMORY
from app.core.planner import Planner

class Assistant:

    def __init__(self):

        self.brain = Brain()
        self.memory = MemoryManager()
        self.personality = Personality()
        self.formatter = ResponseFormatter()
        self.extractor = AIMemory()
        self.tools = ToolManager()
        self.planner = Planner()

    def chat(self, message):

        route = self.planner.route(message)

        # --------------------
        # MEMORY
        # --------------------

        if route == "memory":

            response = self.memory.answer_from_memory(message)

            if response:
                return self.formatter.format(response)

        # --------------------
        # TOOLS
        # --------------------

        elif route == "tool":

            response = self.tools.execute(message)

            if response:
                return self.formatter.format(response)

        # --------------------
        # BRAIN
        # --------------------

        self.memory.add_message("user", message)

        reply = self.brain.think(
            self.memory.get_history()
        )

        self.memory.add_message("model", reply)

        return self.formatter.format(reply)