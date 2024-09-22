from flask import Flask
from flask_cors import CORS
from db.db import *

app = Flask(__name__)
CORS(app)


@app.route('/init_ui/<username>', methods=['GET'])
def init_ui():
    """ client anfrage -> liefert daten für die ui nach db abgleich """
    pass

@app.route('/req_thread/<username>', methods=['GET'])
def req_thread():
    """ client anfrage -> anfrage an serverapp zum start des ExerciseScannerThread """
    pass


if __name__ == '__main__':
    app.run(debug=True)
