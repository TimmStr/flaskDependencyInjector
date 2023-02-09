from flask import Flask
from flask_bootstrap import Bootstrap
from containers import Container
import views


def create_app() -> Flask:
    container = Container()

    app = Flask(__name__)
    app.container = container
    app.add_url_rule("/", "index", views.index)

    bootstrap = Bootstrap()
    bootstrap.init_app(app)
    return app
