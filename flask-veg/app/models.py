from app import db
from sqlalchemy.sql.operators import ColumnOperators

class VegModel(db.Model):
    __tablename__ = 'vegetables'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    colour = db.Column(db.String())
    length = db.Column(db.Integer())

    def __init__(self, name, colour, length):
        self.name = name
        self.colour = colour
        self.length = length

    def __repr__(self):
        return f"<Vegetable {self.name}>"