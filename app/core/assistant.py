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

        if message.lower() == "show plan":

            return "\n".join(
                str(task)
                for task in tasks
            )

        tasks = self.planner.plan(message)

        responses = []

        for task in tasks:
            print(task.type, "->", task.message)

            # --------------------
            # MEMORY
            # --------------------

            if task.type == "memory":

                response = self.memory.answer_from_memory(
                    task.message
                )

                if response:
                    responses.append(
                        self.formatter.format(response)
                    )

            # --------------------
            # TOOLS
            # --------------------

            elif task.type == "tool":

                response = self.tools.execute(
                    task.message
                )

                if response:
                    responses.append(
                        self.formatter.format(response)
                    )

            # --------------------
            # KNOWLEDGE
            # --------------------

            elif task.type == "knowledge":

                context = self.knowledge.ask(
                    task.message
                )

                self.memory.add_message(
                    "user",
                    task.message
                )

                reply = self.brain.think(
                    self.memory.get_history(),
                    context=context
                )

                self.memory.add_message(
                    "model",
                    reply
                )

                responses.append(
                    self.formatter.format(reply)
                )

            # --------------------
            # BRAIN
            # --------------------

            else:

                self.memory.add_message(
                    "user",
                    task.message
                )

                reply = self.brain.think(
                    self.memory.get_history()
                )

                self.memory.add_message(
                    "model",
                    reply
                )

                responses.append(
                    self.formatter.format(reply)
                )

        return "\n\n".join(responses)