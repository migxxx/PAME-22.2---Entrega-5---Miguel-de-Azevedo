from app.models import BaseModel
from app.extensions import db


class Stock(BaseModel):
    __tablename__ = "stock"

    stockID = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    quantidade = db.Column(db.Integer)