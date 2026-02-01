from app.models.base import BaseModel
from app.extensions import db

class City(BaseModel):
    __tablename__ = 'cities'
    name = db.Column(db.String(128), nullable=False)
    state_id = db.Column(db.String(36), db.ForeignKey('states.id'), nullable=False)
    places = db.relationship('Place', backref='city', lazy=True)

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id
