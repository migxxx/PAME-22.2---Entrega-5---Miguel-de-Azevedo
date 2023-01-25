from app.extensions import ma

from .models import Stock

class StockSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Stock
        load_instance = True
        ordered = True

    stockID = ma.Integer(dump_only = True)
    product_id = ma.Integer()
    quantidade = ma.Integer()