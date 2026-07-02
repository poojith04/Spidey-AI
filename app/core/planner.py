from app.core.intent_classifier import IntentClassifier
from app.core.task import Task
from app.core.task_parser import TaskParser


class Planner:

    def __init__(self):

        self.classifier = IntentClassifier()
        self.parser = TaskParser()

    def plan(self, message):

        parts = self.parser.parse(message)

        tasks = []

        for part in parts:

            route = self.classifier.classify(part)

            tasks.append(
                Task(route, part)
            )

        return tasks