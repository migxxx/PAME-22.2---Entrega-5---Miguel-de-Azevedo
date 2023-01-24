from app.models import BaseModel
from app.extensions import db


class Products(BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    estoque = db.Column(db.Integer)