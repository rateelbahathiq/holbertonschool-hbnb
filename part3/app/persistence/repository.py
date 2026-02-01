<<<<<<< HEAD
from app.extensions import db
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

class SQLAlchemyRepository:
    def __init__(self, model):
        self.model = model

    def get(self, id):
        """Get an object by ID"""
        return self.model.query.get(id)

    def get_all(self):
        """Get all objects"""
        return self.model.query.all()

    def add(self, obj):
        """Add a new object to the database"""
        db.session.add(obj)
        db.session.commit()
        return obj

    def update(self, obj_id, data):
        """Update an object by ID"""
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
            db.session.commit()
            return obj
        return None

    def delete(self, obj_id):
        """Delete an object by ID"""
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()
            return True
        return False

    def get_by_attribute(self, attr_name, attr_value):
        """Get an object by a specific attribute (e.g., email)"""
        return self.model.query.filter(getattr(self.model, attr_name) == attr_value).first()
=======
"""
Repository Module
"""
from app.models.base import BaseModel


class InMemoryRepository:
    """
    Generic In-Memory Repository class for temporary storage.
    """
    def __init__(self):
        """Initialize the repository storage."""
        self._storage = {}  # Dictionary to store objects by ID

    def add(self, obj):
        """Add an object to storage."""
        self._storage[obj.id] = obj

    def get(self, obj_id):
        """Get an object by ID."""
        return self._storage.get(obj_id)

    def get_all(self):
        """Get all objects in storage."""
        return list(self._storage.values())

    def update(self, obj_id, data):
        """Update an object by ID."""
        obj = self.get(obj_id)
        if obj:
            obj.update(data)

    def delete(self, obj_id):
        """Delete an object by ID."""
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        """Get an object by a specific attribute."""
        return next(
            (obj for obj in self._storage.values()
             if getattr(obj, attr_name) == attr_value),
            None
        )
>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
