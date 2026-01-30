from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name'),
    'last_name': fields.String(description='Last name'),
    'email': fields.String(description='Email')
})

# Define the input model for Place
place_model = api.model('Place', {
    'id': fields.String(readonly=True, description='Place unique identifier'),
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenity_ids': fields.List(fields.String, required=False,
                               description="List of amenity IDs")
})


@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.marshal_with(place_model, code=201)
    def post(self):
        """Create a new place"""
        place_data = api.payload

        # 1. Validate owner exists
        user = facade.get_user(place_data['owner_id'])
        if not user:
            return {'error': 'Owner not found'}, 400

        # 2. Validate price
        if place_data['price'] < 0:
            return {'error': 'Price must be non-negative'}, 400

        # 3. Extract amenity_ids from the data so they don't cause a crash
        amenity_ids = place_data.pop('amenity_ids', [])

        # 4. Create the place
        new_place = facade.create_place(place_data)

        # 5. Link the amenities to the new place
        for amenity_id in amenity_ids:
            amenity = facade.get_amenity(amenity_id)
            if amenity:
                new_place.add_amenity(amenity)

        return new_place, 201

    @api.marshal_list_with(place_model)
    def get(self):
        """Retrieve all places"""
        return facade.get_all_places()


@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.marshal_with(place_model)
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return place

    @api.expect(place_model)
    @api.marshal_with(place_model)
    def put(self, place_id):
        """Update place details"""
        place_data = api.payload
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        # Example validation for update
        if 'owner_id' in place_data and \
           place_data['owner_id'] != place.owner_id:
            return {'error': 'Cannot change the owner of a place'}, 400

        place.update(place_data)
        return place
