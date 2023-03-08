"""This module has the User model that represnts a single user.

The classes declared:

User:
    A class representing a single user.
"""
from dataclasses import dataclass
from datetime import datetime

from flask import current_app
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer

from ...extensions.extensions import db, ma


@dataclass
class User(db.Model, UserMixin):
    """A class representing a single user."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpeg")
    password = db.Column(db.String(60), nullable=False)
    account_activated = db.Column(db.Boolean, default=False)

    @staticmethod
    def user_with_name_exists(user_name: str) -> bool:
        """Check if user with the name exists.

        Parameters
        ----------
        user_name: str
            The username to check for existance.

        Returns
        -------
        bool:
            True if user with the name exists else False.
        """
        user = User.query.filter_by(username=user_name).first()
        if user:
            return True
        return False

    @staticmethod
    def user_with_email_exists(user_email: str) -> bool:
        """Check if user with the email exists.

        Parameters
        ----------
        user_email: str
            The email to check for existance.

        Returns
        -------
        bool:
            True if user with the email exists else False.
        """
        user = User.query.filter_by(email=user_email).first()
        if user:
            return True
        return False

    def get_reset_token(self):
        """Generate the password reset token."""
        s = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        return s.dumps(
            {"user_id": self.id}, salt=current_app.config["PASSWORD_RESET_SALT"]
        )

    @staticmethod
    def verify_reset_token(token, expires_sec=1800):
        """Verify the password reset token."""
        s = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(
                token,
                salt=current_app.config["PASSWORD_RESET_SALT"],
                max_age=expires_sec,
            )["user_id"]
        except Exception as e:
            print(e)
            return None
        return User.query.get(user_id)
