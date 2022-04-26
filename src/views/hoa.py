from flask import Blueprint
from flask import jsonify, make_response, request
from presenter.hoa import get_all_hoas, add_hoas
import json

hoa_views = Blueprint("hoas", __name__)


@hoa_views.route('/hoas', methods=['GET'])
def get_hoas():
    hoas = get_all_hoas()
    r = []
    for hoa in hoas:
        r.append(hoa.__dict__)
    return make_response(jsonify({"hoas": r}), 200)

@hoa_views.route('/hoas', methods=['POST'])
def add_hoa_view():
    data = str(request.get_data(as_text=True))
    data = json.loads(data)

    if ("hoa_name" not in data) or ("hoa_address" not in data):
        return make_response(jsonify({"status": "bad request"}), 400)

    hoa_name = data["hoa_name"]
    hoa_address = data["hoa_address"]


    add_hoas(hoa_name, hoa_address)
    return make_response(jsonify({"status": "success"}), 201)
