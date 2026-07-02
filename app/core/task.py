class Task:

    def __init__(
        self,
        task_type,
        message,
        priority=0,
        confidence=1.0
    ):

        self.type = task_type
        self.message = message
        self.priority = priority
        self.confidence = confidence

    def __repr__(self):

        return (
            f"Task("
            f"type={self.type}, "
            f"priority={self.priority}, "
            f"confidence={self.confidence:.2f}, "
            f"message='{self.message}')"
            
        )