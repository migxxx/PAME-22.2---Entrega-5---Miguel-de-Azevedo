from app.extensions import ma

from .models import Products

class ProductSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Products
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only = True)
    nome = ma.String(required = True)
    estoque = ma.Integer(required = True)