from flask import url_for, redirect, request, render_template
from ..models.user import User
from ...extensions.extensions import bcrypt, db
from flask_login import login_user, current_user
from ..forms.login import LoginForm


def handle_registration(form):
    """Handle user registration."""
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(
        username=form.username.data,
        email=form.email.data,
        password=hashed_password
    )
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))


def handle_login(form):
    """Handle user login."""
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('home.home_page'))
    return render_template('auth/login.html', title='Login', form=LoginForm())
