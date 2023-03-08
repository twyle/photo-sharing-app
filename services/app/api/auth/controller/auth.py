"""This module hadles user registration, authentication and authorization.

Has the following methods:
handle_create_user:
create_user:
"""
from flask import redirect, render_template, request, url_for

from ...extensions.extensions import bcrypt, db
from ..models.user import User
from .exceptions import (
    EmailAddressExistsException,
    InvalidEmailAddressFormatException,
    InvalidLoginDetails,
    InvalidPasswordFormatException,
    NameExistsException,
    NameTooLongException,
    NameTooShortException,
    PasswordMissmatchException,
    PasswordTooShortException,
)
from .helpers import is_email_address_format_valid, is_password_valid


def create_user(user_data: dict):
    """Handle the post request to create a new user."""
    if len(user_data["name"]) < 2:
        raise NameTooShortException("The user name has to be atleast 2 characters.")
    if len(user_data["name"]) > 20:
        raise NameTooLongException("The user name has to be at most 20 characters.")
    if User.user_with_name_exists(user_data["name"]):
        raise NameExistsException(
            f'A user with the name {user_data["name"]} already exists.'
        )
    if not is_email_address_format_valid(user_data["email"]):
        raise InvalidEmailAddressFormatException("The email address format is invalid.")
    if User.user_with_email_exists(user_data["email"]):
        raise EmailAddressExistsException(
            f'A user with the email {user_data["email"]} already exists.'
        )
    if len(user_data["password"]) < 6:
        raise PasswordTooShortException("The password has to be atleast 6 characters.")
    if not is_password_valid(user_data["password"]):
        raise InvalidPasswordFormatException("The password has to be alphanumeric.")
    if user_data["password"] != user_data["confirm_password"]:
        raise PasswordMissmatchException("The passwords do not match.")
    hashed_password = bcrypt.generate_password_hash(user_data["password"]).decode(
        "utf-8"
    )
    user = User(
        username=user_data["name"], email=user_data["email"], password=hashed_password
    )
    db.session.add(user)
    db.session.commit()


def handle_create_user(user_data: dict):
    """Handle the post request to create a new user."""
    try:
        create_user(user_data=user_data)
    except (NameTooShortException, NameTooLongException, NameExistsException) as e:
        return render_template("auth/register.html", error_message={"name": str(e)})
    except (InvalidEmailAddressFormatException, EmailAddressExistsException) as e:
        return render_template("auth/register.html", error_message={"email": str(e)})
    except (PasswordTooShortException, InvalidPasswordFormatException) as e:
        return render_template("auth/register.html", error_message={"password": str(e)})
    except PasswordMissmatchException as e:
        return render_template(
            "auth/register.html", error_message={"confirm_password": str(e)}
        )

    return redirect(url_for("auth.login"))


def login_user(user_credentials: dict):
    """Log in a registered user.

    Parameters
    ----------
    user_credentials: dict
        The dictionary containing user credentials.
    """
    user = User.query.filter_by(email=user_credentials["email"]).first()
    if user and bcrypt.check_password_hash(user.password, user_credentials["password"]):
        login_user(user)
    else:
        raise InvalidLoginDetails("The login details are invalid.")


def handle_login_user(user_credentials: dict):
    """Handle the POST request to log in a registered user.

    Parameters
    ----------
    user_credentials: dict
        The dictionary containing user credentials.

    Returns
    -------
    tuple: (str, http_response_code)
        Redirect to homepage on successful login or login page on unsuccessfull
        login.
    """
    try:
        login_user(user_credentials)
    except InvalidLoginDetails as e:
        return render_template("auth/login.html", error=str(e))
    next_page = request.args.get("next")
    return redirect(next_page) if next_page else redirect(url_for("home.home_page"))
