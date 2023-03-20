"""This module contains routes for the app."""
from flask import Blueprint, jsonify, redirect, request, url_for
from flask_login import current_user, login_required

from ..utils.http_status_codes import HTTP_200_OK

post = Blueprint("post", __name__)


@post.route("/post", methods=["POST"])
@login_required
def create_post():
    """Create a new post."""
    print(request.form)
    print(request.files)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@post.route("/post", methods=["PUT"])
@login_required
def update_post():
    """Update a post."""
    id = request.args.get("start")
    print(request.form)
    print(id)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@post.route("/post", methods=["DELETE"])
@login_required
def delete_post():
    """Delete a post."""
    id = request.args.get("start")
    print(id)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@post.route("/post", methods=["GET"])
@login_required
def get_post():
    """Get a single post."""
    id = request.args.get("start")
    print(id)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@post.route("/post", methods=["GET"])
@login_required
def get_posts():
    """Get many post post."""
    start = request.args.get("start")
    count = request.args.get("count")
    author = request.args.get("author")
    category = request.args.get("category")
    print(start)
    print(count)
    print(author)
    print(category)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@post.route("/like", methods=["GET"])
@login_required
def like_post():
    """Like a single post."""
    id = request.args.get("start")
    print(id)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@post.route("/likes", methods=["GET"])
@login_required
def get_post_likes():
    """Get a posts likes."""
    id = request.args.get("start")
    start = request.args.get("start")
    count = request.args.get("count")
    print(id)
    print(start)
    print(count)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@post.route("/bookmark", methods=["GET"])
@login_required
def like_bookmark():
    """Bookmark a single post."""
    id = request.args.get("start")
    print(id)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@post.route("/comment", methods=["GET"])
@login_required
def comment_post():
    """Comment on a single post."""
    id = request.args.get("start")
    print(id)
    return jsonify({"Resp": "greate"}), HTTP_200_OK


@post.route("/comments", methods=["GET"])
@login_required
def get_post_comments():
    """Get a posts comments."""
    id = request.args.get("start")
    start = request.args.get("start")
    count = request.args.get("count")
    print(id)
    print(start)
    print(count)
    return jsonify({"Resp": "greate"}), HTTP_200_OK
