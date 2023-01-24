from flask import Blueprint

from .controllers import *

products_api = Blueprint("products_api", __name__)

products_api.add_url_rule(
    "/products",
    view_func = ProductController.as_view("products_controller"),
    methods = ["GET", "POST"]
)