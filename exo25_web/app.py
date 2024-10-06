from flask import Flask, g


def create_app() -> Flask:
    from .blueprints import home, browse, create, learn

    app = Flask(__name__)

    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(browse, url_prefix="/browse")
    app.register_blueprint(create, url_prefix="/create")
    app.register_blueprint(learn, url_prefix="/learn")

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, "_database", None)
        if db is not None:
            db.close()

    return app
