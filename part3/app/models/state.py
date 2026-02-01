from app.models.base import BaseModel
from app.extensions import db

class State(BaseModel):
    __tablename__ = 'states'
    name = db.Column(db.String(128), nullable=False)
    cities = db.relationship('City', backref='state', lazy=True)

    def __init__(self, name):
        self.name = name
