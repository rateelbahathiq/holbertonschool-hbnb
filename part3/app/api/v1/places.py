from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Review text'),
    'rating': fields.Integer(description='Rating'),
    'user_id': fields.String(description='Author ID')
})

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, description="List of amenity IDs")
})

place_output_model = api.model('PlaceOutput', {
    'id': fields.String(description='Place ID'),
    'title': fields.String(description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(description='Price per night'),
    'latitude': fields.Float(description='Latitude of the place'),
    'longitude': fields.Float(description='Longitude of the place'),
    'owner_id': fields.String(description='ID of the owner'),
    'created_at': fields.DateTime(description='Creation timestamp'),
    'updated_at': fields.DateTime(description='Update timestamp'),
    'owner': fields.Nested(user_model, description='Owner details'),
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

@api.route('/')
class PlaceList(Resource):
    @api.doc('list_places')
    @api.marshal_list_with(place_output_model)
    def get(self):
        return facade.get_all_places()

    @api.doc('create_place')
    @api.expect(place_model)
    @api.marshal_with(place_output_model, code=201)
    def post(self):
        place_data = api.payload
        amenity_ids = place_data.pop('amenities', [])
        new_place = facade.create_place(place_data)
        for amenity_id in amenity_ids:
            facade.add_amenity_to_place(new_place.id, amenity_id)
        return facade.get_place(new_place.id), 201

@api.route('/<place_id>')
@api.param('place_id', 'The Place identifier')
@api.response(404, 'Place not found')
class PlaceResource(Resource):
    @api.doc('get_place')
    @api.marshal_with(place_output_model)
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, "Place not found")
        return place

    @api.doc('update_place')
    @api.expect(place_model)
    @api.marshal_with(place_output_model)
    def put(self, place_id):
        place_data = api.payload
        place = facade.update_place(place_id, place_data)
        if not place:
            api.abort(404, "Place not found")
        return place

@api.route('/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.doc('get_place_reviews')
    @api.marshal_list_with(review_model)
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, "Place not found")
        return facade.get_reviews_by_place(place_id)
