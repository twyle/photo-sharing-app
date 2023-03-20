"""This module hadles user registration, authentication and authorization.

Has the following methods:
handle_create_user:
create_user:
"""
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user

from ...extensions.extensions import bcrypt, db
from ..models.user import User
from .exceptions import (
    EmailAddressExistsException,
    EmailDoesNotExistsException,
    InvalidEmailAddressFormatException,
    InvalidPasswordFormatException,
    InvalidToken,
    NameExistsException,
    NameTooLongException,
    NameTooShortException,
    PasswordMissmatchException,
    PasswordTooShortException,
)
from .helpers import (
    is_email_address_format_valid,
    is_password_valid,
    send_confirm_account_email,
    send_reset_password_email,
)


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
    send_confirm_account_email(user_data["email"])


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


def handle_send_confirm_account_email(email: str):
    """Send the account activation email."""
    send_confirm_account_email(email)
    return redirect(url_for("auth.login"))


def handle_confirm_account(token: str):
    """Activate a user account."""
    user = User.verify_reset_token(token)
    if not user:
        print(f"That is an invalid or expired token! {token}")
        flash(
            "That is an invalid or expired token! Another one has been sent to your email."
        )
        return redirect(url_for("auth.login"))
    user.account_activated = True
    db.session.commit()
    return redirect(url_for("auth.login"))


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
    user = User.query.filter_by(email=user_credentials["email"]).first()
    if user and not user.account_activated:
        return render_template(
            "auth/login.html",
            error_message="Your account is not activated.",
            email=user.email,
        )
    if user and bcrypt.check_password_hash(user.password, user_credentials["password"]):
        login_user(user)
        next_page = request.args.get("next")
        return redirect(next_page) if next_page else redirect(url_for("home.home_page"))
    return render_template(
        "auth/login.html", error_message="Invalid username or password."
    )


def reset_request(user_data: dict):
    """Send the password reset email.

    Parameters
    ----------
    user_data: dict
        The user details, in this case the email.
    """
    if not is_email_address_format_valid(user_data["email"]):
        raise InvalidEmailAddressFormatException("The email address format is invalid.")
    if not User.user_with_email_exists(user_data["email"]):
        raise EmailDoesNotExistsException(
            f'There is no user with email {user_data["email"]}.'
        )
    send_reset_password_email(user_data["email"])
    flash("An email has been sent with instructions on how to rewset your password!")
    return redirect(url_for("auth.reset_password"))


def handle_reset_request(user_data: dict):
    """Handle the request to rest the user password.

    Parameters
    ----------
    user_data: dict
        The user details, in this case the email.
    """
    try:
        return reset_request(user_data)
    except (InvalidEmailAddressFormatException, EmailDoesNotExistsException) as e:
        return render_template("auth/resetrequest.html", error_message=str(e))


def reset_password(token: str, user_data: dict):
    """Reset the user password.

    token: str
        The password reset token.
    user_data: dict
        The dictionary containing the new password.
    """
    user = User.verify_reset_token(token)
    if not user:
        raise InvalidToken("That is an invalid or expired token!")
    if len(user_data["password"]) < 6:
        raise PasswordTooShortException("The password has to be atleast 6 characters.")
    if not is_password_valid(user_data["password"]):
        raise InvalidPasswordFormatException("The password has to be alphanumeric.")
    if user_data["password"] != user_data["confirm_password"]:
        raise PasswordMissmatchException("The passwords do not match.")
    hashed_password = bcrypt.generate_password_hash(user_data["password"]).decode(
        "utf-8"
    )
    user.password = hashed_password
    db.session.commit()
    flash("Your password has been updated. You are now able to log in!")
    return redirect(url_for("auth.login"))


def handle_reset_password(token: str, user_data: dict):
    """Handle the POST request to reset the user password.

    token: str
        The password reset token.
    user_data: dict
        The dictionary containing the new password.
    """
    try:
        return reset_password(token, user_data)
    except InvalidToken as e:
        return render_template("auth/resetpassword.html", errors={"token": str(e)})
    except (PasswordTooShortException, InvalidPasswordFormatException) as e:
        return render_template("auth/resetpassword.html", errors={"password": str(e)})
    except PasswordMissmatchException as e:
        return render_template(
            "auth/resetpassword.html", errors={"confirm_password": str(e)}
        )
