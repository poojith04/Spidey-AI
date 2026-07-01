class Memory:
    def __init__(self):
        self.history = []

    def add(self, role, message):
        self.history.append({
            "role": role,
            "parts": [{"text": message}]
        })

    def get(self):
        return self.history

    def clear(self):
        self.history = []