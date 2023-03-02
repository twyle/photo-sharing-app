from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app() -> Flask:
    """Create the Flask App instance."""
    app = Flask(__name__)
    
    @app.route('/health')
    def home():
        return 'Hello world!'
    
    app.shell_context_processor({'app': app})
    
    return app