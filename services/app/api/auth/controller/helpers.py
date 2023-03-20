"""This module declares helper methods for the auth package."""
import re
import string

from flask import url_for
from flask_mail import Message

from ...extensions.extensions import mail
from ..models.user import User
from .exceptions import InvalidEmailAddressFormatException, InvalidPasswordFormatException


def is_email_address_format_valid(email_address: str) -> bool:
    """Check if email address is valid.

    Parameters
    ----------
    email_address: str
        The email address to check.

    Raises
    ------
    InvalidEmailAddressFormatException:
        If the email address is not provided

    Returns
    -------
    bool:
        True if email address is valid else False
    """
    if not email_address:
        raise InvalidEmailAddressFormatException("The email address format is invalid.")

    #  Regular expression for validating an Email
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    if re.fullmatch(regex, email_address):
        return True
    return False


def is_password_valid(password: str) -> bool:
    """Check if the password is valid.

    Parameters
    ----------
    password: str
        The password string to check.

    Raises
    ------
    InvalidPasswordFormatException:
        If the password is not provided.

    Returns
    -------
    bool:
        True if password is valid else False
    """
    password_is_numbers = (
        password.isnumeric() or password.isdecimal() or password.isdigit()
    )
    # uppercase = 0
    # numbers = 0
    # punctuation = 0
    if not password:
        raise InvalidPasswordFormatException("The password has to be alphanumeric.")
    if not password.isascii() or not password.isalnum() or password_is_numbers:
        return False
    # for character in password:
    #     if character.isnumeric() or character.isdecimal() or character.isdigit():
    #         numbers += 1
    #     elif character.isupper():
    #         uppercase += 1
    #     elif character in string.punctuation or string.whitespace:
    #         punctuation += 1
    # if not uppercase:
    #     print('No uppercase')
    #     return False
    # if not numbers:
    #     print('No numbers')
    #     return False
    # if not punctuation:
    #     print('No punctuation')
    #     return False
    return True


def send_email(user: User, email_type: str):
    """Send an email to the given user.

    Parameters
    ----------
    user: User
        A registered user.
    email_type: str
        The email type to send. Can be account confirmation
        or password rest.
    """
    if email_type == "account_confirmation":
        email_body = {
            "header": "Account Activation Email",
            "body": "Click on the following link to activate your account.",
            "url": "auth.confirm_account",
        }
    else:
        email_body = {
            "header": "Password Reset Email",
            "body": "Click on the following link to reset your account password.",
            "url": "auth.reset_password",
        }
    token = user.get_reset_token()
    msg = Message(
        email_body["header"], sender="lyceokoth@gmail.com", recipients=[user.email]
    )
    link = url_for(email_body["url"], token=token, _external=True)
    msg.body = f"{email_body['body']}{link}"
    mail.send(msg)


def send_confirm_account_email(email_address: str):
    """Send the user registration email.

    Parameters
    ----------
    email_address: str
        The users email address.
    """
    user = User.query.filter_by(email=email_address).first()
    send_email(user, "account_confirmation")
    return "Email account confirm email."


def send_reset_password_email(email_address: str):
    """Send the password reset email email.

    Parameters
    ----------
    email_address: str
        The users email address.
    """
    user = User.query.filter_by(email=email_address).first()
    send_email(user, "password_reset")
    return "Password reset email."
