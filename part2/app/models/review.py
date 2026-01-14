"""
Review Model Module
"""
from app.models.base import BaseModel


class Review(BaseModel):
    """
    Represents a review for a place in the HBnB application.
    """
    def __init__(self, text, rating, place_id, user_id):
        """Initialize a new Review instance."""
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    @property
    def rating(self):
        """Getter for rating."""
        return self._rating

    @rating.setter
    def rating(self, value):
        """Setter for rating. Ensures value is between 1 and 5."""
        if 1 <= value <= 5:
            self._rating = value
        else:
            raise ValueError("Rating must be between 1 and 5")
