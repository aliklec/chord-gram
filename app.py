from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin  # to get UI to work
import markdown2
from app.services import Services

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/parse": {"origins": "http://localhost:port"}})

service = Services()

@app.route("/common", methods=["GET"])
def show_common():
    output = service.show_common_chord_combos()
    return jsonify(output)

@app.route("/generate", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def generate_chords():
    start_chord = request.get_json()
    chords = service.make_sequence(start_chord)
    return jsonify(chords)

@app.route("/doc", methods=["GET"])
def doc():
    with open("documents/documentation.md", "r") as f:
        content = f.read()
    html = markdown2.markdown(content)
    return html

@app.route("/", methods=["GET"])
def readme():
    with open("README.md", "r") as f:
        content = f.read()
    html = markdown2.markdown(content)
    return html

# @app.route("/c-chord", methods=["GET"])
# def show_c():
#     output = service.c_start()
#     return jsonify(output)

# IN DEVELOPMENT
@app.route("/chordinfo", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def chord_info():
    data = request.get_json()
    chord = service.make_chord(data['root'], data['chordType'], data.get('bass'))
    return jsonify(chord)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')

