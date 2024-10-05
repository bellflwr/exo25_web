from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello exoworld"
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run("localhost", 8000, debug=True)
