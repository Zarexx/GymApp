from flask import Flask, request, render_template, Response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    msg = str(request.data)
    print(msg)
    return render_template("index.html", test=msg)


@app.route('/video_feed', methods=['GET', 'POST'])
def video_feed():
    msg = str(request.data)
    print(msg)
    return msg


if __name__ == '__main__':
    app.run(debug=True)
