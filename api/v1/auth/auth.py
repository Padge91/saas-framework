
from flask import Blueprint, jsonify

auth_app = Blueprint("auth_app", __name__)


@auth_app.route("/login", methods=["POST"])
def login():
    return False


@auth_app.route("/logout", methods=["POST"])
def logout():
    return False


@auth_app.route("/reset", methods=["POST"])
def reset_password():
    return False