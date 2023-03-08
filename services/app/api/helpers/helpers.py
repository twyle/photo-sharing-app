"""This module delares helper methods for the whole app.

Declares the following config:

set_configuration:
    For setting the apps configuration.
register_blueprints:
    For registering the application blueprints.
register_extensions:
    For registering the application extensions.
"""
import os

from dotenv import load_dotenv
from flask import Flask

from ..auth.views import auth
from ..config.config import Config

from ..extensions.extensions import (
    db,
    ma,
    bcrypt,
    migrate,
    cors,
    login_manager
)

load_dotenv()


def set_configuration(app):
    """Set the application configuration.

    The application configuration will depend on the
    environment i.e Test, Development, Staging or Production.

    Parameters
    ----------
    app: flask.Flask
        A flask app instance

    Returns
    -------
    bool:
        Whether the config was set up successfully.
    """
    config_name = os.environ.get("FLASK_ENV", "development")
    app.config.from_object(Config[config_name])

    return True


def register_blueprints(app: Flask) -> bool:
    """Register the application blueprints.

    Parameters
    ----------
    app: flask.Flask
        A flask app instance

    Returns
    -------
    bool:
        Whether all the blueprints were registered.
    """
    app.register_blueprint(auth, url_prefix="/auth")
    return True


def register_extensions(app: Flask):
    """Register the app extensions."""
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
