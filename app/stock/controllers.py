# GENERAL GET / DETAILS GET, POST / BUY PATCH

from flask import request
from flask.views import MethodView

from .models import Stock
from .schemas import StockSchema

from app.products.models import Products

# /products/stock
class StockController(MethodView):
    def get(self):
        schema = StockSchema()

        stock = Stock.query.all()
        return schema.dump(stock, many = True), 200

# /products/<id>/stock
class StockProductController(MethodView):
    def get(self, product_id):
        schema = StockSchema()

        product = Products.query.get(product_id)
        if not product:
            return {}, 404

        productStock = product.stock

        return schema.dump(productStock, many= True), 200


    def post(self, product_id):
        schema = StockSchema()

        product = Products.query.get(product_id)
        if not product:
            return {}, 404

        if product.stock:
            return {"error": "product already registrated"}, 401

        data = request.json
        data["product_id"] = product_id

        try:
            addStock = schema.load(data)
        except:
            return {}, 400

        addStock.save()
        return schema.dump(addStock), 201


# /products/<id>/stock/<id>
class StockDetails(MethodView):             # alterar a quantidade de estoque de um produto
                                            # usada também para compra
    def patch(self, product_id, stockID):
        schema = StockSchema()

        product = Products.query.get(product_id)
        if not product:
            return {"error": "product not found"}, 404

        stockProduct = Stock.query.get(stockID)
        if not stockProduct:
            return {"error": "stock not found"}, 404

        if stockProduct.product_id != product_id:
            return {"error": "permission denied"}, 401

        data = request.json

        try:
            editStock = schema.load(data, instance=stockProduct, partial = True)
        except:
            return {}, 400

        editStock.save()
        return schema.dump(editStock), 201
    
    def delete(self, product_id, stockID):

        product = Products.query.get(product_id)
        if not product:
            return {"error": "product not found"}, 404

        stockProduct = Stock.query.get(stockID)
        if not stockProduct:
            return {"error": "stock not found"}, 404

        if stockProduct.product_id != product_id:
            return {"error": "permission denied"}, 401

        stockProduct.delete(stockProduct)
        return {}, 204