# emotional_tags.py

def tag_emotion(message):
    message = message.lower()
    if "happy" in message or "joy" in message:
        return "😊"
    elif "sad" in message or "lonely" in message:
        return "🌧️"
    elif "dream" in message or "hope" in message:
        return "🌠"
    else:
        return "✨"
