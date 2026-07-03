# aiva/emotional_tags.py
emotion_to_emoji = {
    "tired": "😴",
    "hopeful": "🌈",
    "hurt": "💔",
    "lonely": "🌧️",
    "confused": "❓",
    "happy": "😊",
    "grateful": "🙏",
    "excited": "🎉",
    "angry": "🔥",
    "sad": "😢",
    "peaceful": "🌿",
    "curious": "🔍",
}

def tag_emotion(message):
    message = message.lower()
    for emotion, emoji in emotion_to_emoji.items():
        if emotion in message:
            return emoji
    return "✨"

def emotion_to_emoji(feeling):
    return emotion_to_emoji.get(feeling.lower(), "✨")
