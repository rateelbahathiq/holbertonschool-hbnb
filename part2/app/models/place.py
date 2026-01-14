"""
Place Model Module
"""
from app.models.base import BaseModel


class Place(BaseModel):
    """
    Represents a place (listing) in the HBnB application.
    """
    def __init__(self, title, description, price, latitude, longitude,
                 owner_id):
        """Initialize a new Place instance."""
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
