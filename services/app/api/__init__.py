"""The main application package."""
from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def create_app() -> Flask:
    """Create the Flask App instance."""
    app = Flask(__name__)

    @app.route("/health")
    def home():
        return "Hello world!", 200

    app.shell_context_processor({"app": app})

    return app
