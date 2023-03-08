"""The main application package."""
from dotenv import load_dotenv
from flask import Flask

from .helpers.helpers import register_blueprints, set_configuration, register_extensions
from .utils.http_status_codes import HTTP_200_OK
from .extensions.extensions import db, login_manager
from .auth.models.user import User

load_dotenv()


def create_app() -> Flask:
    """Create the Flask App instance."""
    app = Flask(__name__)
    set_configuration(app)
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
