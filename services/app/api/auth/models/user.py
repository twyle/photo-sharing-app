from ...extensions.extensions import db, ma
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer
from flask import current_app


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    
    @staticmethod
    def user_with_name_exists(user_name: str) -> bool:
        """Check if user with the name exists."""
        user = User.query.filter_by(username=user_name).first()
        if user:
            return True
        return False
    
    @staticmethod
    def user_with_email_exists(user_email: str) -> bool:
        """Check if user with the name exists."""
        user = User.query.filter_by(email=user_email).first()
        if user:
            return True
        return False
    
    def get_reset_token(self):
        s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id}, salt=current_app.config['PASSWORD_RESET_SALT'])

    @staticmethod
    def verify_reset_token(token, expires_sec=1800):
        s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, salt=current_app.config['PASSWORD_RESET_SALT'], max_age=expires_sec)['user_id']
        except Exception as e:
            print(e)
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}', image_file='{self.image_file}')"
