"""A module containing user views."""
from flask import Blueprint, jsonify, request
from flask_login import login_required

from ..utils.http_status_codes import HTTP_200_OK

user = Blueprint("user", __name__)


@user.route("/befriend", methods=["GET"])
@login_required
def befriend():
    """Befriend a given person.."""
    user_id = request.args.get("id")
    person_to_befriend = request.args.get("id")
    print(user_id)
    print(person_to_befriend)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@user.route("/unfriend", methods=["GET"])
@login_required
def unfriend():
    """Unfriend a given person.."""
    user_id = request.args.get("id")
    person_to_unfriend = request.args.get("id")
    print(user_id)
    print(person_to_unfriend)
    return jsonify({"Resp": "greater"}), HTTP_200_OK


@user.route("/message", methods=["GET"])
@login_required
def send_message():
    """Send a friend a message."""
    sender_id = request.args.get("id")
    sendee_id = request.args.get("id")
    print(sender_id)
    print(sendee_id)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@user.route("/messages", methods=["GET"])
@login_required
def get_messages():
    """Get a particular users messages.."""
    user_id = request.args.get("id")
    print(user_id)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@user.route("/notifications", methods=["GET"])
@login_required
def get_notifications():
    """Get a particular users notifications.."""
    user_id = request.args.get("id")
    print(user_id)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@user.route("/bookmarks", methods=["GET"])
@login_required
def get_bookmarks():
    """Get a particular users bookmarks.."""
    user_id = request.args.get("id")
    print(user_id)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@user.route("/requests", methods=["GET"])
@login_required
def get_requests():
    """Get a particular users friend requests."""
    user_id = request.args.get("id")
    print(user_id)
    return jsonify({"Resp": "greate"}), HTTP_200_OK
