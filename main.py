import json

from flask import Flask, jsonify, request, abort
from model.twit import Twit

twits = []
twits_id = []

app = Flask(__name__)


def id_gen():
    match len(twits_id):
        case 0:
            twit_id = 1
            twits_id.append(twit_id)
            return twit_id
        case _:
            twit_id = len(twits_id) + 1
            twits_id.append(twit_id)
            return twit_id


@app.route('/twit', methods=['GET'])
def read_twits():
    return jsonify({'twits': [twit.to_dict() for twit in twits]})


@app.route('/twit/<int:twit_id>', methods=['GET'])
def read_twit(twit_id):
    twit = next((twit for twit in twits if twit.twit_id == twit_id), None)
    if twit is None:
        abort(404)
    return jsonify(twit.to_dict())


@app.route('/twit', methods=['POST'])
def create_twit():
    if not request.json or not 'body' in request.json or not 'author' in request.json:
        abort(400)
    twit = Twit(id_gen(), request.json['body'], request.json['author'])
    twits.append(twit)
    return jsonify({'status': 'success'}), 201


@app.route('/twit/<int:twit_id>', methods=['PUT'])
def update_twit(twit_id):
    twit = next((twit for twit in twits if twit.twit_id == twit_id), None)
    if twit is None:
        abort(404)
    if not request.json:
        abort(400)
    if 'body' in request.json:
        twit.body = request.json['body']
    if 'author' in request.json:
        twit.author = request.json['author']
    return jsonify({'status': 'success'})


@app.route('/twit/<int:twit_id>', methods=['DELETE'])
def delete_twit(twit_id):
    twit = next((twit for twit in twits if twit.twit_id == twit_id), None)
    if twit is None:
        abort(404)
    twits.remove(twit)
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)