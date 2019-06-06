from datetime import datetime

from flask import Flask, jsonify, render_template

from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/api/hello', methods=["GET", ])
def hello():
    return 'Hello World from Taohid!'


@app.route('/api/time', methods=["GET", ])
def current_time_api():
    return jsonify(datetime.now())


@app.route("/", methods=["GET", ])
def index():
    return render_template("index.html")


@app.route("/time", methods=["GET", ])
def current_time():
    return render_template("time.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
