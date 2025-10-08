# aiva_memory.py

class AivaMemory:
    def __init__(self):
        self.log = []

    def record_message(self, speaker, message):
        self.log.append((speaker, message))

    def get_last(self):
        return self.log[-1] if self.log else None
