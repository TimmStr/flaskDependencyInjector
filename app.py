from flask import Flask
from flask_bootstrap import Bootstrap
from containers import Container
import views


def create_app() -> Flask:
    container = Container()
    container.config.github.auth_token.from_env("cbde697a6e01424856fde2b7f94a88d1b501320e")

    app = Flask(__name__)
    app.container = container
    app.add_url_rule("/", "index", views.index)

    bootstrap = Bootstrap()
    bootstrap.init_app(app)
    return app
