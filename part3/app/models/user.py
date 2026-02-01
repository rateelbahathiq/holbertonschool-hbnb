<<<<<<< HEAD
from app.models.base import BaseModel
from app.extensions import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(BaseModel):
    __tablename__ = 'users'

    # Database Columns (Mapped to private attributes for validation)
    _first_name = db.Column("first_name", db.String(50), nullable=False)
    _last_name = db.Column("last_name", db.String(50), nullable=False)
    _email = db.Column("email", db.String(120), unique=True, nullable=False)
    
    # Simple columns (no validation property needed for these)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Relationships (Links to other tables)
    places = db.relationship('Place', backref='owner', lazy=True)
    reviews = db.relationship('Review', backref='author', lazy=True)

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        # We don't call super().__init__() because db.Model doesn't need it.
        # We set attributes directly to trigger the @property setters below.
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        # Hashing happens here automatically
        self.password_hash = generate_password_hash(password).decode('utf8')

    @property
    def first_name(self):
        """Getter for first_name."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """Setter for first_name. Validates length."""
        if not value or len(value) > 50:
            raise ValueError("First name must be 50 characters or less")
        self._first_name = value

    @property
    def last_name(self):
        """Getter for last_name."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """Setter for last_name. Validates length."""
        if not value or len(value) > 50:
            raise ValueError("Last name must be 50 characters or less")
        self._last_name = value

    @property
    def email(self):
        """Getter for email."""
        return self._email

    @email.setter
    def email(self, value):
        """Setter for email. Validates simple format."""
        if not value or "@" not in value or "." not in value:
            raise ValueError("Invalid email format")
        self._email = value

    def verify_password(self, password):
        """Verifies the input password against the stored hash."""
        return check_password_hash(self.password_hash, password)
=======
"""
User Model Module
"""

from app.models.base import BaseModel
from app.extensions import bcrypt


class User(BaseModel):
    """
    Represents a user in the HBnB application.
    """

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = None
        self.is_admin = is_admin
        self.places = []
        self.reviews = []

    def set_password(self, password):
        """Hash and store the password"""
        self.password_hash = bcrypt.generate_password_hash(
            password
        ).decode('utf-8')

    def check_password(self, password):
        """Verify a password"""
        return bcrypt.check_password_hash(self.password_hash, password)

>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
