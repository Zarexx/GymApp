from flask import Flask, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import cv2

import db.db as db


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)


def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        frame_as_text = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_as_text + b'\r\n')

# Websocket

@socketio.on('request_frames')
def handle_request_frames():
    def event_stream():
        for frame in generate_frames():
            yield frame
    socketio.emit('frame', event_stream(), namespace='/')

@socketio.on('request_frames')
def send_message(m):
    pass
# Api 

@app.route('/init_ui/<username>', methods=['GET'])
def init_ui(username):
    """ client anfrage -> liefert daten für die ui nach db abgleich """
    return db.user_1

if __name__ == '__main__':
    app.run(debug=True, port=5002)
