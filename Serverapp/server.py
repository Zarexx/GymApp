from flask import Flask

app = Flask(__name__)


@app.route('/init')
def req_start():
    return 0


