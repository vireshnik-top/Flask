import json

from flask import Flask, jsonify, request, abort
from model.twit import Twit

twits = []

app = Flask(__name__)


@app.route('/twit', methods=['POST'])
def create_twit():
    if not request.json or not 'body' in request.json or not 'author' in request.json:
        abort(400)
    twit = Twit(request.json['body'], request.json['author'])
    twits.append(twit)
    return jsonify({'status': 'success'}), 201

@app.route('/twit', methods=['GET'])
def read_twits():
    # Используйте метод to_dict для преобразования объектов Twit в словари
    return jsonify({'twits': [twit.to_dict() for twit in twits]})




if __name__ == '__main__':
    app.run(debug=True)
