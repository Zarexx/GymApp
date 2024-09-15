from flask import Flask

app = Flask(__name__)


@app.route('/req_start')
def req_start():
    """c1 weiterleitung an serverapp (Schritt 2)"""
    return 0


