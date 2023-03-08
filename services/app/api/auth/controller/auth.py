"""This module hadles user registration, authentication and authorization.

Has the following methods:
handle_create_user:
create_user:
"""
from flask import redirect, render_template, url_for

from .exceptions import (
    EmailAddressExistsException,
    InvalidEmailAddressFormatException,
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
    # Check if name exists.
    if not is_email_address_format_valid(user_data["email"]):
        raise InvalidEmailAddressFormatException("The email address format is invalid.")
    # Check if email exists.
    if len(user_data["password"]) < 6:
        raise PasswordTooShortException("The password has to be atleast 6 characters.")
    if not is_password_valid(user_data["password"]):
        raise InvalidPasswordFormatException("The password has to be alphanumeric.")
    if user_data["password"] != user_data["confirm_password"]:
        raise PasswordMissmatchException("The passwords do not match.")


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
