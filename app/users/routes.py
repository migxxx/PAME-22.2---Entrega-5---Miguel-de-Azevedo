from flask import Blueprint

from .controllers import *

user_api = Blueprint("user_api", __name__)

user_api.add_url_rule(
    "/users",
    view_func = UserController.as_view("users_controller"),
    methods = ["GET", "POST"]
)

user_api.add_url_rule(
    "/users/<int:id>",
    view_func = UserDetails.as_view("users_details"),
    methods = ["GET", "PUT", "PATCH", "DELETE"]
)