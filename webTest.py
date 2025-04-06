import flask

from flask import request, jsonify, Response

app = flask.Flask(__name__)
counter = 0
@app.route('/')
def index():
    global counter
    if request.method == 'GET':
        if counter % 2 == 0:
            counter += 1
            return jsonify({'msg': 'even'}), 200
        elif counter % 2 == 1:
            counter += 1
            return jsonify({'msg': 'odd'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=33333, debug=True)
