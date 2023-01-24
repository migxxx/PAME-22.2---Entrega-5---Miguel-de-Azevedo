from flask import request
from flask.views import MethodView

from .schemas import ProductSchema
from .models import Products

# /products
class ProductController(MethodView):
    def get(self):
        pass

    def post(self):
        pass

# /products/<id>
class ProductDetails(MethodView):

    def put(self, productID): # ideia: modificar o produto
        pass

    def patch(self, productID): # ideia: comprar o produto
        pass

    def delete(self, productID):
        pass