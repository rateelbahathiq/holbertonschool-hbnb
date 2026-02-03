from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.extensions import db

class HBnBFacade:
    def get_user(self, user_id):
        return User.query.get(user_id)

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        db.session.add(user)
        db.session.commit()
        return user

    def get_place(self, place_id):
        return Place.query.get(place_id)

    def create_place(self, place_data):
        place = Place(**place_data)
        db.session.add(place)
        db.session.commit()
        return place

    def get_all_places(self):
        return Place.query.all()

    def update_place(self, place_id, place_data):
        place = Place.query.get(place_id)
        if not place:
            return None
        for key, value in place_data.items():
            if key != 'id':
                setattr(place, key, value)
        db.session.commit()
        return place

    def get_amenity(self, amenity_id):
        return Amenity.query.get(amenity_id)

    def get_all_amenities(self):
        return Amenity.query.all()

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        db.session.add(amenity)
        db.session.commit()
        return amenity

    def update_amenity(self, amenity_id, amenity_data):
        amenity = Amenity.query.get(amenity_id)
        if not amenity:
            return None
        if 'name' in amenity_data:
            amenity.name = amenity_data['name']
        db.session.commit()
        return amenity
    
    def add_amenity_to_place(self, place_id, amenity_id):
        place = Place.query.get(place_id)
        amenity = Amenity.query.get(amenity_id)
        if place and amenity:
            place.add_amenity(amenity)
            db.session.commit()

    def create_review(self, review_data):
        review = Review(**review_data)
        db.session.add(review)
        db.session.commit()
        return review

    def get_review(self, review_id):
        return Review.query.get(review_id)

    def get_all_reviews(self):
        return Review.query.all()

    def get_reviews_by_place(self, place_id):
        place = Place.query.get(place_id)
        if not place:
            return []
        return place.reviews

    def update_review(self, review_id, review_data):
        review = Review.query.get(review_id)
        if not review:
            return None
        for key, value in review_data.items():
            if key != 'id':
                setattr(review, key, value)
        db.session.commit()
        return review

    def delete_review(self, review_id):
        review = Review.query.get(review_id)
        if review:
            db.session.delete(review)
            db.session.commit()
