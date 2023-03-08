"""The main application package."""
from dotenv import load_dotenv
from flask import Flask

from .helpers.helpers import register_blueprints, set_configuration
from .utils.http_status_codes import HTTP_200_OK

load_dotenv()


def create_app() -> Flask:
    """Create the Flask App instance."""
    app = Flask(__name__)
    set_configuration(app)
    register_blueprints(app=app)

    @app.route("/health")
    def home():
        return "Hello world!", HTTP_200_OK

    app.shell_context_processor({"app": app})

    return app
