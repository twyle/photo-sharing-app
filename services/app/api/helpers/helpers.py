"""This module delares helper methods for the whole app.

Declares the following config:

set_configuration:
    For setting the apps configuration.
register_blueprints:
    For registering the application blueprints.
register_extensions:
    For registering the application extensions.
"""
from flask import Flask

from ..auth.views import auth


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
