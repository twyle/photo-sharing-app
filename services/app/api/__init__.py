"""The main application package."""
# import sys

from dotenv import load_dotenv
from flask import Flask

from .auth.models.user import User
from .exceptions.exceptions import DatabaseNotConnectedException
from .extensions.extensions import db, login_manager
from .helpers.helpers import (
    check_configuration,
    register_blueprints,
    register_extensions,
    set_configuration,
)
from .utils.http_status_codes import HTTP_200_OK

load_dotenv()


def create_app() -> Flask:
    """Create the Flask App instance."""
    app = Flask(__name__)

    set_configuration(app)

    try:
        check_configuration()
    except DatabaseNotConnectedException as e:
        print(str(e))
        # sys.exit(1)

    register_extensions(app)
    register_blueprints(app=app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route("/health")
    def home():
        return "Hello world!", HTTP_200_OK

    app.shell_context_processor({"app": app, "db": db})

    return app
