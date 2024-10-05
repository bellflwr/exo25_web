from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello exoworld"
    
    return app
