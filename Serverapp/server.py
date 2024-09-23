from ScannerUtils.scanner import start_thread

from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)


@app.route('/init_thread')
def init_thread():
    """Initalize den ExerciseScanner thread
        - Baut websocket verbindung mit Client auf 
        - Startet den ExerciseScanner thread
    """
    # nicht fertig / websocket fehlt
    start_thread("chestpress")
    return "True"


if __name__ == '__main__':
    socketio.run(app, port=5001)
