from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place'),
    'created_at': fields.DateTime(description='Creation timestamp'),
    'updated_at': fields.DateTime(description='Update timestamp')
})

review_create_model = api.model('ReviewCreate', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.doc('create_review')
    @api.expect(review_create_model)
    @api.marshal_with(review_model, code=201)
    @jwt_required()
    def post(self):
        """Create a new review"""
        current_user_id = get_jwt_identity()
        data = api.payload
        place_id = data.get('place_id')

        place = facade.get_place(place_id)
        if not place:
            api.abort(404, "Place not found")

        # Logic: User cannot review their own place
        if place.owner_id == current_user_id:
            return {'message': 'You cannot review your own place'}, 400

        # Logic: User cannot review a place twice
        if facade.get_review_by_user_and_place(current_user_id, place_id):
            return {'message': 'You have already reviewed this place'}, 400

        data['user_id'] = current_user_id
        review = facade.create_review(data)
        return review, 201

    @api.doc('list_reviews')
    @api.marshal_list_with(review_model)
    def get(self):
        """List all reviews"""
        return facade.get_all_reviews()

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.doc('get_review')
    @api.marshal_with(review_model)
    def get(self, review_id):
        """Fetch a review given its identifier"""
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Review not found")
        return review

    @api.doc('update_review')
    @api.expect(review_create_model)
    @api.marshal_with(review_model)
    @jwt_required()
    def put(self, review_id):
        """Update a review"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)

        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Review not found")

        # Logic: Only owner or admin can update
        if review.user_id != current_user_id and not is_admin:
             return {'message': 'Unauthorized action'}, 403

        review = facade.update_review(review_id, api.payload)
        return review

    @api.doc('delete_review')
    @api.response(204, 'Review deleted')
    @jwt_required()
    def delete(self, review_id):
        """Delete a review"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)
        
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Review not found")

        # Logic: Only owner or admin can delete
        if review.user_id != current_user_id and not is_admin:
             return {'message': 'Unauthorized action'}, 403

        facade.delete_review(review_id)
        return '', 204
