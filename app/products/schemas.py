from app.extensions import ma
from app.stock.schemas import StockSchema

from .models import Products

class ProductSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Products
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only = True)
    nome = ma.String(required = True)
    tipo = ma.String(required = True)

    stock = ma.List(ma.Nested(StockSchema(exclude=["product_id", "stockID"])), dump_only=True)