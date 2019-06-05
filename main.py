from datetime import datetime
import os

from flask import Flask, jsonify, render_template

from flask_cors import CORS

app = Flask(__name__, static_folder='hello-world-frontend/build/static', template_folder="hello-world-frontend/build")

CORS(app)


@app.route('/', methods=["GET", ])
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World from Taohid!'


@app.route("/current_time", methods=["GET", ])
def current_time():
    return jsonify(datetime.now())


@app.route('/time', methods=["GET", ])
def serve():
    print(app.static_folder)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
