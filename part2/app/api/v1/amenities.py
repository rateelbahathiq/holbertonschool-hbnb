from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Amenity model for input/output
amenity_model = api.model('Amenity', {
    'id': fields.String(readonly=True, description='Amenity unique identifier'),
    'name': fields.String(required=True, description='Name of the amenity'),
    'description': fields.String(required=False,
                                 description='Description of the amenity')
})


@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.marshal_with(amenity_model, code=201)
    def post(self):
        """Create a new amenity"""
        amenity_data = api.payload
        new_amenity = facade.create_amenity(amenity_data)
        return new_amenity, 201

    @api.marshal_list_with(amenity_model)
    def get(self):
        """Retrieve all amenities"""
        return facade.get_all_amenities()


@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        return amenity

    @api.expect(amenity_model)
    @api.marshal_with(amenity_model)
    def put(self, amenity_id):
        """Update amenity details"""
        amenity_data = api.payload
        updated_amenity = facade.update_amenity(amenity_id, amenity_data)
        if not updated_amenity:
            return {'error': 'Amenity not found'}, 404
        return updated_amenity
