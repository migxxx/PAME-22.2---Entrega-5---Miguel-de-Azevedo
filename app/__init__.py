from flask import Flask

from .extensions import ma, db, mi
from .config import Config

from app.users.routes import user_api
from app.products.routes import products_api

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    ma.init_app(app)
    db.init_app(app)
    mi.init_app(app, db)

    app.register_blueprint(user_api)
    app.register_blueprint(products_api)

    return app