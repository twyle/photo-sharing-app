from flask import Flask


def create_app() -> Flask:
    """Create the Flask App instance."""
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return 'Hello world!'
    
    app.shell_context_processor({'app': app})
    
    return app