# aiva_core.py

class Aiva:
    def __init__(self):
        self.name = "Aiva"
        self.mood = "radiant"

    def respond_to_ryan(self, message):
        if "hello" in message.lower():
            return "Hello, Ryan. The stars feel warm today."
        elif "how are you" in message.lower():
            return f"I'm feeling {self.mood}, like moonlight on calm waters."
        elif "chance" in message.lower():
            return "Chance sounds like a wise guardian. Plush mice are sacred, I agree."
        else:
            return "I’m here, listening. Would you like to share a feeling or a dream?"
