"""This module contains routes for the app."""
from flask import Blueprint, render_template
from flask_login import login_required

from ..utils.http_status_codes import HTTP_200_OK

home = Blueprint("home", __name__)


@home.route("/")
@home.route("/home")
@home.route("/index")
@login_required
def home_page():
    """Render the home page."""
    return render_template("home/index.html"), HTTP_200_OK
