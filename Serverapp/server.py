from ScannerUtils.scanner import start_thread

from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)


@app.route('/init_thread/<ip>')
def init_thread(ip):
    """Initalize den ExerciseScanner thread
        - Baut websocket verbindung mit Client auf 
        - Startet den ExerciseScanner thread
    """
    print(ip)
    # start_thread("chestpress")
    return f"{ip}" 


if __name__ == '__main__':
    socketio.run(app, port=5001)
