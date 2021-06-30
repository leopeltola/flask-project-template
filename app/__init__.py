from flask import Flask

from config import Config


def create_app(config_class=Config):
    """
    Application factory. Returns a Flask object created from the config class
    """

    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.errors import bp as errors_bp

    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp

    app.register_blueprint(main_bp)

    return app
