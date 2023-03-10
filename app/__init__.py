from flask import Flask

from .extensions import ma, db, mi, jwt
from .config import Config

from app.users.routes import user_api
from app.products.routes import products_api
from app.stock.routes import stock_api

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    ma.init_app(app)
    db.init_app(app)
    mi.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(user_api)
    app.register_blueprint(products_api)
    app.register_blueprint(stock_api)

    return app