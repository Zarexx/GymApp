from flask import Flask

app = Flask(__name__)


@app.route('/start_thread')
def req_start():
    return 0


