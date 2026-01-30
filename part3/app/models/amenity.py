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
