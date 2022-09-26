from flask import Flask
from flask_restx import Api
from app.database import db
from app.config import Config
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()

    return application


def configure_app(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


if __name__ == '__main__':
    app = create_app(Config())
    configure_app(app)
    app.run(host="localhost", port=10001)
