from flask import Flask

def create_app() -> Flask:
    from .blueprints import home

    app = Flask(__name__)

    app.register_blueprint(home, url_prefix="/")
    
    return app
