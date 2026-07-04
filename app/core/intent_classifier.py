class IntentClassifier:

    def classify(self, message):

        message = message.lower()

        # --------------------
        # Memory
        # --------------------

        memory_words = [
            "my name",
            "favorite",
            "goal",
            "college",
            "editor"
        ]

        if any(word in message for word in memory_words):
            return "memory"

        # --------------------
        # Knowledge
        # --------------------

        knowledge_words = [
            "my notes",
            "my pdf",
            "my documents",
            "according to",
            "from my notes",
            "from my pdf",
            "study material",
            "uploaded document"
        ]

        if any(word in message for word in knowledge_words):
            return "knowledge"

        # --------------------
        # Tools
        # --------------------

        tool_words = [
            "open",
            "launch",
            "create",
            "delete",
            "close",
            "shutdown",
            "restart"
        ]

        if any(word in message for word in tool_words):
            return "tool"

        return "brain"
    def classify_with_router(self, message, router):

        route = self.classify(message)

        if route != "brain":
            return route

        if router.should_use_knowledge(message):
            return "knowledge"

        return "brain"