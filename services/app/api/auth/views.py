"""This module contains the view functions for authorization.

Declares the following methods:

register:
    Register a new user.
send_confirm_account_email:
    Send the user registration email.
confirm_account:
    Confirm the user account.
login:
    Login a registered user.
logout:
    Logout a logged in user
reset_request:
    Handle the request to reset the password.
reset_password:
    Reset the user password
send_reset_email:
    Send the password reset email
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for

from ..utils.http_status_codes import HTTP_200_OK, HTTP_307_TEMPORARY_REDIRECT
from .controller.auth import handle_create_user

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user."""
    if request.method == "POST":
        return handle_create_user(request.form)
    return render_template("auth/register.html"), HTTP_200_OK


def send_confirm_account_email():
    """Send the user registration email."""
    return "Email account confirm email."


@auth.route("/confirm_account", methods=["GET"])
def confirm_account():
    """Confirm a newly created account."""
    # get userid and token
    return "Acount confirmed.", HTTP_200_OK


@auth.route("/login", methods=["GET", "POST"])
def login():
    """Login a registered user."""
    # ensure account is confirmed
    return render_template("auth/login.html"), HTTP_200_OK


@auth.route("/reset_request", methods=["GET", "POST"])
def reset_request():
    """Handle the request to reset the password."""
    return render_template("auth/resetrequest.html"), HTTP_200_OK


@auth.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    """Reset the user password."""
    return render_template("auth/resetpassword.html"), HTTP_200_OK


@auth.route("/logout", methods=["GET"])
def logout():
    """Logout a logged in user."""
    return redirect(url_for("auth.login")), HTTP_307_TEMPORARY_REDIRECT
