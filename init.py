from flask import Flask
from handlers.feed_handler import FEED

from config import CONFIG
from models import db


def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = CONFIG['SQLALCHEMY_TRACK_MODIFICATIONS']
    db.init_app(app)
    app.register_blueprint(FEED)

    return app

