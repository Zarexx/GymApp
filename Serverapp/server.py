from flask import Flask
from ScannerUtils.scanner import Starter
app = Flask(__name__)


def start_thread():
    gym = Starter()
    gym.rep("chestpress", 0)


@app.route('/init')
def req_start():
    print("Teststart")
    start_thread()
    return {"Serverapp": "starte application"}


if __name__ == '__main__':
    app.run(debug=True, port=5001)
