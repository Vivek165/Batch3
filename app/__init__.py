"""Flask application factory for the monitoring demo."""

from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev-only-change-me",
    )

    from app.routes import bp

    app.register_blueprint(bp)
    return app
