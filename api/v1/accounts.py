
from flask import Blueprint, jsonify

accounts_app = Blueprint("accounts_app", __name__)


@accounts_app.route("/join", methods=["POST"])
def join_account():
    return False


@accounts_app.route("/leave", methods=["POST"])
def leave_account():
    return False


@accounts_app.route("/promote", methods=["POST"])
def promote_owner():
    return False


@accounts_app.route("/kick", methods=["POST"])
def kick_user():
    return False


@accounts_app.route("/register", methods=["POST"])
def register_account():
    return False


@accounts_app.route("/invite_user", methods=["POST"])
def accept_invite():
    return False


@accounts_app.route("/upgrade_account", methods=["POST"])
def accept_invite():
    return False


@accounts_app.route("/downgrade_account", methods=["POST"])
def accept_invite():
    return False