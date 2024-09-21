#from ScannerUtils.scanner import start_thread

from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/init')
def req_start():
    print("Teststart")
    start_thread("chestpress", )
    return {"Serverapp": "starte application"}

@socketio.on("connect")
def connected():
    """event listener when client connects to the server"""
    print("client has connected")

@socketio.on('test')
def handle_message(data):
    print('Empfangene Nachricht:', data)
    emit('response', {'data': 'Nachricht erhalten!'})


if __name__ == '__main__':
       socketio.run(app, port=5001)

