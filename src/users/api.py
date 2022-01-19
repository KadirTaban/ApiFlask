import os
import firebase_admin.auth
import google
from flask import json, request, jsonify
from src.users.models import Users
from app import app


@app.route('/v1/users/add', methods=['POST'])
def user_add():
    veri = request.get_json()
    user = Users()

    user.uuid = veri['uuid']
    user.name = veri['name']
    user.surname = veri['surname']
    user.skill = veri['skill']

    user.add_user()

    return jsonify("user created"), 200


@app.route('/v1/users/get', methods=['GET'])
def get_user():
    uuid = request.json.get('uuid')
    user = Users().get_user(uuid)

    if uuid is None:
        return jsonify({"error": "uuid cannot be None"})
    jsonUser = json.dumps(user.__dict__)
    return jsonUser


@app.route('/v1/users/update', methods=['PUT'])
def update_user():
    veri = request.get_json()
    user = Users()
    user.get_user(veri['uuid'])
    key = user.key

    user.uuid = veri['uuid']
    user.name = veri['name']
    user.surname = veri['surname']
    user.skill = veri['skill']
    user.update_user(key)
    return jsonify({'message': 'user updated.'}), 200


@app.route('/v1/users/delete', methods=['DELETE'])
def delete_user():
    veri = request.get_json()
    user = Users().get_user(veri['uuid'])
    user.delete_user()

    return jsonify({'message': 'user deleted'}), 200
