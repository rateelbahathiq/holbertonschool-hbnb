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
