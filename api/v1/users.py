
from flask import Blueprint, jsonify

users_app = Blueprint("users_app", __name__)


@users_app.route("/register", methods=["POST"])
def register():
    return False


@users_app.route("/login", methods=["POST"])
def login():
    return False


@users_app.route("/logout", methods=["POST"])
def logout():
    return False


@users_app.route("/reset_password", methods=["POST"])
def reset_password():
    return False


@users_app.route("/reset_password_confirm", methods=["POST"])
def reset_password():
    return False
