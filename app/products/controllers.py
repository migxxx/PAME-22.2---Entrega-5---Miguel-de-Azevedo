from flask import request
from flask.views import MethodView

from .schemas import ProductSchema
from .models import Products

#from app.stock.controllers import StockProductController
#from app.stock.schemas import StockSchema
#from app.stock.controllers import StockDetails
#from app.stock.models import Stock

# /products
class ProductController(MethodView):
    def get(self):
        schema = ProductSchema()
        products = Products.query.all()

        return schema.dump(products, many=True), 200

    def post(self):
        schema = ProductSchema()
        data = request.json

        try:
            product = schema.load(data)
            #print(product)
        except:
            return {}, 400

        # call stock class, to save the product in stock
        
        
        #stock = StockProductController()
        #dump = stockSchema.load(product)

        #stock.post(dump["id"])

        product.save()

        return schema.dump(product), 201

# /products/<id>
class ProductDetails(MethodView):

    def get(self,id):
        schema = ProductSchema()

        product = Products.query.get(id)
        if not product:
            return {"error": "product not found"}, 404
        
        return schema.dump(product), 200

    def put(self, id):
        schema = ProductSchema()

        product = Products.query.get(id)
        if not product:
            return {"error": "product not found"}, 404
        
        data = request.json
        try:
            product = schema.load(data, instance=product)
        except:
            return {}, 400

        product.save()
        return schema.dump(product), 201


    def patch(self, id):
        schema = ProductSchema()

        product = Products.query.get(id)
        if not product:
            return {"error": "product not found"}, 404
        
        data = request.json
        
        try:
            product = schema.load(data, instance=product, partial = True) # partial = True, significa que o dado pode ser mudado parcialmente, mantendo suas outras caracteristicas
        except:
            return {}, 400

        product.save()
        return schema.dump(product), 201


    def delete(self, id):                               # para deletar um produto é necessário deletar primeiro do Estoque, e depois deletar nos produtos
                                                        # caso não faça, o estoque terá como product_id == null
        product = Products.query.get(id)
        if not product:
            return {"error": "product not found"}, 404

        # stock = StockDetails()
        # stock.delete(id, id)

        product.delete(product)
        
        return{}, 204                                       

# /products/<type>
class FilterByProductType(MethodView):

    def get(self, type):
        schema = ProductSchema()

        product = Products.query.filter(Products.tipo.endswith(type)).all()
        # print(product)
        if not product:
            return {"error": "type of product does not exist"}, 404

        return schema.dump(product, many=True), 200