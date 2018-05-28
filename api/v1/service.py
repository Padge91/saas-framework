
from flask import Blueprint, jsonify

service_app = Blueprint("service_app", __name__)


@service_app.route("/submit_ticket", methods=["POST"])
def register():
    return False
