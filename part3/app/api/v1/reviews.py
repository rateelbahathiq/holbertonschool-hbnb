from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input
review_model = api.model('Review', {
    'id': fields.String(readonly=True, description='Review unique identifier'),
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True,
                             description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})


@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.marshal_with(review_model, code=201)
    def post(self):
        """Create a new review"""
        review_data = api.payload

        # 1. Validate User exists
        user = facade.get_user(review_data['user_id'])
        if not user:
            return {'error': 'User not found'}, 400

        # 2. Validate Place exists
        place = facade.get_place(review_data['place_id'])
        if not place:
            return {'error': 'Place not found'}, 404

        # 3. Validate Rating
        if not (1 <= review_data['rating'] <= 5):
            return {'error': 'Rating must be between 1 and 5'}, 400

        new_review = facade.create_review(review_data)

        # Link review to place
        place.add_review(new_review)

        return new_review, 201

    @api.marshal_list_with(review_model)
    def get(self):
        """Retrieve all reviews"""
        return facade.get_all_reviews()


@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.marshal_with(review_model)
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return review

    @api.expect(review_model)
    @api.marshal_with(review_model)
    def put(self, review_id):
        """Update review details"""
        review_data = api.payload
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        review.update(review_data)
        return review

    def delete(self, review_id):
        """Delete a review"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        facade.delete_review(review_id)
        return {'message': 'Review deleted successfully'}, 200


@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.marshal_list_with(review_model)
    def get(self, place_id):
        """Get all reviews for a specific place"""
        # Validate place exists
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        return facade.get_reviews_by_place(place_id)
