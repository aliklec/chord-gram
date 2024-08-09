from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin  # to get UI to work
from logging.config import dictConfig

from app.services import Services

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/parse": {"origins": "http://localhost:port"}})

service = Services()


@app.route("/generate", methods=["GET"])
def show_probs():
    output = service.show_probs()
    return output


if __name__ == '__main__':
    app.run(host='0.0.0.0')
