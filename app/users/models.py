from app.models import BaseModel
from app.extensions import db


class Users(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    cargo = db.Column(db.String(20))