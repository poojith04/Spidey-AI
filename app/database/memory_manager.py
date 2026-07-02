from app.database.conversation_memory import Memory
from storage.sqlite_memory import SQLiteMemory


class MemoryManager:

    def __init__(self):
        self.conversation = Memory()
        self.long_term = SQLiteMemory()

    # ------------------------
    # Conversation Memory
    # ------------------------

    def add_message(self, role, message):
        self.conversation.add(role, message)

    def get_history(self):
        return self.conversation.get()

    def clear_history(self):
        self.conversation.clear()

    # ------------------------
    # Long-Term Memory
    # ------------------------

    def remember(self, key, value):
        self.long_term.remember(key, value)

    def recall(self, key):
        return self.long_term.recall(key)
    def answer_from_memory(self, message):

        message = message.lower()

        if "what's my name" in message or "what is my name" in message:
            name = self.recall("name")
            if name:
                return f"Boss, your name is {name.title()} 😎"

        if "favorite language" in message:
            language = self.recall("favorite_language")
            if language:
                return f"Your favorite programming language is {language.title()} 🚀"

        if "college" in message:
            college = self.recall("college")
            if college:
                return f"You study at {college.title()} 🎓"

        if "goal" in message:
            goal = self.recall("goal")
            if goal:
                return f"Your goal is {goal} 💪"

        if "editor" in message:
            editor = self.recall("editor")
            if editor:
                return f"You use {editor.title()} as your editor 💻"

        return None