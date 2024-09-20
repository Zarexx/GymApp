from flask import Flask, jsonify
from flask_cors import CORS
import requests
from db.db import *

app = Flask(__name__)
CORS(app)


@app.route('/init_ui', methods=['GET'])
def init_ui():
    """ client anfrage -> liefert daten für die ui
        Ablauf
            - eingehender request
            - verbindungsüberprüfung - serverapp via ping
            - datenbank verbindung, abfrage
            - zurückgabe der daten
    """
    response = requests.get('http://127.0.0.1:5001/init')
    return response.text


if __name__ == '__main__':
    app.run(debug=True)
