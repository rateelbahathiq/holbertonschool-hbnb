"""
Review Model Module
"""
from app.models.base import BaseModel
<<<<<<< HEAD
from app.extensions import db

class Review(BaseModel):
    """
    Represents a review written by a user for a place.
    This model links to both the 'users' and 'places' tables.
    """
    __tablename__ = 'reviews'

    # Database Columns
    _text = db.Column("text", db.Text, nullable=False)
    _rating = db.Column("rating", db.Integer, nullable=False)

    # --- THE FIX: Foreign Keys required by SQLAlchemy ---
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    def __init__(self, text, rating, place_id, user_id):
        """Initialize a new Review instance."""
=======


class Review(BaseModel):
    """
    Represents a review for a place in the HBnB application.
    """
    def __init__(self, text, rating, place_id, user_id):
        """Initialize a new Review instance."""
        super().__init__()
>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    @property
<<<<<<< HEAD
    def text(self):
        """Getter for review text."""
        return self._text

    @text.setter
    def text(self, value):
        """Setter for review text. Ensures it is not empty."""
        if not value or len(value.strip()) == 0:
            raise ValueError("Review text cannot be empty")
        self._text = value

    @property
=======
>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
    def rating(self):
        """Getter for rating."""
        return self._rating

    @rating.setter
    def rating(self, value):
<<<<<<< HEAD
        """Setter for rating. Validates range 1-5."""
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5")
        self._rating = value
=======
        """Setter for rating. Ensures value is between 1 and 5."""
        if 1 <= value <= 5:
            self._rating = value
        else:
            raise ValueError("Rating must be between 1 and 5")
>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
