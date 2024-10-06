from flask import Flask

def create_app() -> Flask:
    from .blueprints import home, browse, create, learn

    app = Flask(__name__)

    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(browse, url_prefix="/browse")
    app.register_blueprint(create, url_prefix="/create")
    app.register_blueprint(learn, url_prefix="/learn")
    
    return app
