from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World from Taohid!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


@app.route("/current_time")
def current_time():
    return jsonify(datetime.now())
