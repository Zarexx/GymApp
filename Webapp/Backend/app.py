from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import cv2
import base64


from ScannerUtils.chestpress import frame_queue, chat_message_queue
from ScannerUtils.chestpress import start_loop, stop_loop
from ScannerUtils.scanner import exercise_chooser

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)

cap = cv2.VideoCapture(0)


def encode_frame(frame):
    _, buffer = cv2.imencode('.jpg', frame)
    encoded_frame = base64.b64encode(buffer).decode('utf-8')
    return encoded_frame

@socketio.on('error')
def emit_chat_message(message):
    """Sendet Fehler an alle verbundenen Clients."""
    socketio.emit('error', message)

@socketio.on('request_frame')
def handle_frame_request():
    if not frame_queue.empty():
        frame = frame_queue.get()
        encoded_frame = encode_frame(frame)
        emit('video_frame', encoded_frame)

@socketio.on('request_chat_message')
def handle_chat_message_request():
    if not chat_message_queue.empty():
        message = chat_message_queue.get()
        print(message)
        emit('chat_message', message)

@app.route('/api/thread_start/<exercise>', methods=['GET'])
def button_click(exercise):
    exercise_chooser(exercise)
    return jsonify({"message": "Button was clicked!"})

@app.route('/api/thread_stop', methods=['GET'])
def button_click2():
    stop_loop()
    return jsonify({"message": "Button was clicked!"})



# Api

@app.route('/init_ui/<username>', methods=['GET'])
def init_ui(username):
    """ client anfrage -> liefert daten für die ui nach db abgleich """
    pass


if __name__ == '__main__':
    app.run(debug=True, port=5002)
