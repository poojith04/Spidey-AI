from app.core.brain import Brain
from app.database.memory_manager import MemoryManager
from app.personality.personality import Personality
from app.formatting.formatter import ResponseFormatter
from app.database.ai_memory import AIMemory
from app.tools.tool_manager import ToolManager
from app.core.planner import Planner
from app.knowledge.knowledge_engine import KnowledgeEngine

class Assistant:

    def __init__(self):

        self.brain = Brain()
        self.memory = MemoryManager()
        self.personality = Personality()
        self.formatter = ResponseFormatter()
        self.extractor = AIMemory()
        self.tools = ToolManager()
        self.planner = Planner()
        self.knowledge = KnowledgeEngine()
        self.knowledge.index("knowledge")

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
        # KNOWLEDGE
        # --------------------

        elif route == "knowledge":

            context = self.knowledge.ask(message)

            self.memory.add_message("user", message)

            reply = self.brain.think(
                self.memory.get_history(),
                context=context
            )

            self.memory.add_message("model", reply)

            return self.formatter.format(reply)
        # --------------------
        # BRAIN
        # --------------------

        self.memory.add_message("user", message)

        reply = self.brain.think(
            self.memory.get_history()
        )

        self.memory.add_message("model", reply)

        return self.formatter.format(reply)