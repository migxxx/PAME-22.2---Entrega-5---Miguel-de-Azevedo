from flask import Blueprint

from .controllers import *

products_api = Blueprint("products_api", __name__)

products_api.add_url_rule(
    "/products",
    view_func = ProductController.as_view("products_controller"),
    methods = ["GET", "POST"]
)

products_api.add_url_rule(
    "/products/<int:id>",
    view_func = ProductDetails.as_view("products_details"),
    methods = ["GET", "PUT", "PATCH", "DELETE"]
)

products_api.add_url_rule(
    "/products/<string:type>",
    view_func = FilterByProductType.as_view("filterProductType_controller"),
    methods = ["GET"]
)