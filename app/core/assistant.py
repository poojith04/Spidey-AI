from app.core.brain import Brain
from app.core.knowledge_router import KnowledgeRouter
from app.database.memory_manager import MemoryManager
from app.personality.personality import Personality
from app.formatting.formatter import ResponseFormatter
from app.database.ai_memory import AIMemory
from app.tools.tool_manager import ToolManager
from app.core.planner import Planner
from app.knowledge.knowledge_engine import KnowledgeEngine
from app.utils.logger import logger

class Assistant:

    def __init__(self):

        self.brain = Brain()

        self.memory = MemoryManager()

        self.personality = Personality()
        self.formatter = ResponseFormatter()

        self.extractor = AIMemory()

        self.tools = ToolManager()
        self.knowledge = KnowledgeEngine()
        self.knowledge.index("knowledge")
        self.router = KnowledgeRouter(self.knowledge)
        self.planner = Planner()

    def chat(self, message):

        if message.lower() == "show plan":

            return "\n".join(
                str(task)
                for task in tasks
            )

        if message.lower().startswith("show plan"):
            command="show plan"

            plan_message = message[len(command):].strip()

            tasks = self.planner.plan(plan_message)

            return "\n".join(str(task) for task in tasks)

        tasks = self.planner.plan(message)
        
        responses = []

        for task in tasks:
            logger.info(f"{task.type} -> {task.message}")

            # --------------------
            # MEMORY
            # --------------------
            try:
                if task.type == "memory":

                    response = self.memory.answer_from_memory(
                        task.message
                    )

                    if response:
                        responses.append(response)

                # --------------------
                # TOOLS
                # --------------------

                elif task.type == "tool":

                    response = self.tools.execute(
                        task.message
                    )

                    if response:
                        responses.append(response)

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

                    responses.append(reply)

                # --------------------
                # BRAIN
                # --------------------

                                # --------------------
                # BRAIN
                # --------------------

                else:

                    decision = self.router.route(task.message)

                    print(
                        f"KnowledgeRouter: "
                        f"use={decision.use_knowledge}, "
                        f"distance={decision.distance}"
                    )

                    self.memory.add_message(
                        "user",
                        task.message
                    )

                    if decision.use_knowledge:

                        reply = self.brain.think(
                            self.memory.get_history(),
                            context=decision.results
                        )

                    else:

                        reply = self.brain.think(
                            self.memory.get_history()
                        )

                    self.memory.add_message(
                        "model",
                        reply
                    )

                    responses.append(reply)
            except Exception as e:
                logger.exception(e)

                responses.append(
                    "Something went wrong while I was working on that task."
                )
        combined = "\n\n".join(responses)

        return self.formatter.format(combined)