"""
User Model Module
"""
from app.models.base import BaseModel


class User(BaseModel):
    """
    Represents a user in the HBnB application.
    """
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """Initialize a new User instance."""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.places = []
        self.reviews = []
