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
from flask_login import current_user, login_required, logout_user

from ..utils.http_status_codes import HTTP_200_OK, HTTP_307_TEMPORARY_REDIRECT
from .controller.auth import (
    handle_confirm_account,
    handle_create_user,
    handle_login_user,
    handle_reset_password,
    handle_reset_request,
    handle_send_confirm_account_email,
)

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user."""
    if current_user.is_authenticated:
        return redirect(url_for("home.home_page"))
    if request.method == "POST":
        # hadle the image
        return handle_create_user(request.form)
    return render_template("auth/register.html"), HTTP_200_OK


@auth.route("/send_confirm_account_email", methods=["GET"])
def send_confirm_account_email():
    """Send account confirmation email."""
    email = request.args.get("email")
    return handle_send_confirm_account_email(email)


@auth.route("/confirm_account", methods=["GET"])
def confirm_account():
    """Confirm a newly created account."""
    if current_user.is_authenticated:
        return redirect(url_for("home.home_page"))
    token = request.args.get("token")
    return handle_confirm_account(token)


@auth.route("/login", methods=["GET", "POST"])
def login():
    """Login a registered user."""
    if current_user.is_authenticated:
        return redirect(url_for("home.home_page"))
    if request.method == "POST":
        return handle_login_user(request.form)
    return render_template("auth/login.html"), HTTP_200_OK


@auth.route("/reset_request", methods=["GET", "POST"])
def reset_request():
    """Handle the request to reset the password."""
    if current_user.is_authenticated:
        return redirect(url_for("home.home_page"))
    if request.method == "POST":
        return handle_reset_request(request.form)
    return render_template("auth/resetrequest.html"), HTTP_200_OK


@auth.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    """Reset the user password."""
    if current_user.is_authenticated:
        return redirect(url_for("home.home_page"))
    if request.method == "POST":
        return handle_reset_password(request.args.get("token"), request.form)
    return render_template("auth/resetpassword.html"), HTTP_200_OK


@login_required
@auth.route("/logout", methods=["GET"])
def logout():
    """Logout a logged in user."""
    logout_user()
    return redirect(url_for("auth.login")), HTTP_307_TEMPORARY_REDIRECT
