from app.extensions import db

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

    def update(self, obj, data):
        """Update an object"""
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        db.session.commit()
        return obj

    def delete(self, obj):
        """Delete an object"""
        db.session.delete(obj)
        db.session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        """Get an object by a specific attribute (e.g., email)"""
        return self.model.query.filter(getattr(self.model, attr_name) == attr_value).first()
