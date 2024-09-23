from flask import Flask
from flask_cors import CORS
import requests

import db.db as db

app = Flask(__name__)
CORS(app)


@app.route('/init_ui/<username>', methods=['GET'])
def init_ui(username):
    """ client anfrage -> liefert daten für die ui nach db abgleich """
    return db.user_1


@app.route('/req_thread/<username>', methods=['GET'])
def req_thread(username):
    """ client anfrage -> anfrage an serverapp zum start des ExerciseScannerThread """
    # nicht fertig
    url = "http://127.0.0.1:5001/init_thread"
    response = requests.get(url)

    if response.status_code == 200:
        return "Starte Thread"
    else:
        return "Felher beim Starten"


if __name__ == '__main__':
    app.run(debug=True)
