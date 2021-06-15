from flask import Flask
from flask_migrate import Migrate

from config import CONFIG
from models import db

from handlers.feed_handler import FEED


def init_app():
    def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = CONFIG['SQLALCHEMY_TRACK_MODIFICATIONS']
    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(AUTHENTICATION)

    return app

