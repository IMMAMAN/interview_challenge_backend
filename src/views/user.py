from flask import Blueprint
from flask import jsonify, make_response, request
from presenter.user import get_all_users, add_user, get_user_by_id
import json

user_views = Blueprint("user", __name__)


@user_views.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    r = []
    for user in users:
        r.append(user.__dict__)
    return make_response(jsonify({"users": r}), 200)

@user_views.route('/users', methods=['POST'])
def add_user_view():
    data = str(request.get_data(as_text=True))
    data = json.loads(data)

    if "user_name" not in data:
        return make_response(jsonify({"status": "bad request"}), 400)

    user_name = data["user_name"]

    add_user(user_name)
    return make_response(jsonify({"status": "success"}), 201)

@user_views.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if(user == None):
        return make_response(jsonify({"status": "user not found"}), 400)
    else:
        return make_response(jsonify(user.__dict__), 200)
