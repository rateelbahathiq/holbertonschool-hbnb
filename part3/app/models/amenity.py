<<<<<<< HEAD
from app.models.base import BaseModel
from app.extensions import db

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    _name = db.Column("name", db.String(50), nullable=False)

    def __init__(self, name, description=""):
        self.name = name
        # We don't save description in DB for this simple model, 
        # but the init expects it for compatibility
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Amenity name cannot be empty")
        self._name = value
=======
"""
Amenity Model Module
"""
from app.models.base import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity (feature) in the HBnB application.
    """
    def __init__(self, name, description=""):
        """Initialize a new Amenity instance."""
        super().__init__()
        self.name = name
        self.description = description
>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
