# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from aiva.aiva_core import Aiva
from aiva.aiva_memory import AivaMemory
from aiva.emotional_tags import tag_emotion

app = Flask(__name__)
socketio = SocketIO(app)

aiva = Aiva()
memory = AivaMemory()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('user_message')
def handle_message(message):
    memory.record_message("Ryan", message)
    response = aiva.respond_to_ryan(message)
    emoji = tag_emotion(message)
    full_response = f"{response} {emoji}"
    memory.record_message("Aiva", full_response)
    emit('aiva_response', full_response)

return render_template("index.html", response=response, emotion="excited")

if __name__ == '__main__':
    socketio.run(app, debug=True)

app.run(debug=True, port=5000)


