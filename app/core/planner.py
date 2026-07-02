class Planner:

    def route(self, message):

        message = message.lower()

        # Memory questions
        if any(word in message for word in [
            "my name",
            "favorite",
            "goal",
            "college",
            "editor"
        ]):
            return "memory"
        
        if any(word in message for word in [

            "my notes",
            "my pdf",
            "my documents",
            "according to",
            "from my notes",
            "from my pdf"

        ]):
            return "knowledge"

        # Tool commands
        if any(message.startswith(cmd) for cmd in [
            "open",
            "create",
            "delete",
            "launch",
            "close",
            "shutdown",
            "restart"
        ]):
            return "tool"

        # Everything else
        return "brain"
        