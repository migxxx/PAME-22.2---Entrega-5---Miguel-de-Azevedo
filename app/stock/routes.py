from flask import Blueprint

from .controllers import *

stock_api = Blueprint("stock_api", __name__)

stock_api.add_url_rule(
    "/stock",
    view_func = StockController.as_view("stock_controller"),
    methods = ["GET"]
)

stock_api.add_url_rule(
    "/products/<int:product_id>/stock",
    view_func = StockProductController.as_view("stockProduct_controller"),
    methods = ["GET", "POST"]
)

stock_api.add_url_rule(
    "/products/<int:product_id>/stock/<int:stockID>",
    view_func = StockDetails.as_view("stock_details"),
    methods = ["PATCH","DELETE"]
)