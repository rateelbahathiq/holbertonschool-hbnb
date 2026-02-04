from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import SQLAlchemyRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = SQLAlchemyRepository(User)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)
        self.amenity_repo = SQLAlchemyRepository(Amenity)

    # --- USER ---
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        return self.user_repo.add(user)

    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if user:
            return self.user_repo.update(user, user_data)
        return None
    
    def get_all_users(self):
        return self.user_repo.get_all()

    # --- PLACE ---
    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def create_place(self, place_data):
        place = Place(**place_data)
        return self.place_repo.add(place)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if place:
            return self.place_repo.update(place, place_data)
        return None

    # --- AMENITY ---
    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        return self.amenity_repo.add(amenity)

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if amenity:
            return self.amenity_repo.update(amenity, amenity_data)
        return None
    
    def add_amenity_to_place(self, place_id, amenity_id):
        place = self.get_place(place_id)
        amenity = self.get_amenity(amenity_id)
        if place and amenity:
            place.add_amenity(amenity)
            # No explicit save needed if session handles it, but repo update commits
            self.place_repo.update(place, {}) 
            return place
        return None

    # --- REVIEW ---
    def create_review(self, review_data):
        review = Review(**review_data)
        return self.review_repo.add(review)

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.get_place(place_id)
        if not place:
            return []
        return place.reviews

    def get_review_by_user_and_place(self, user_id, place_id):
        # Specific query needed for duplicate check
        return Review.query.filter_by(user_id=user_id, place_id=place_id).first()

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)
        if review:
            return self.review_repo.update(review, review_data)
        return None

    def delete_review(self, review_id):
        review = self.get_review(review_id)
        if review:
            self.review_repo.delete(review)
