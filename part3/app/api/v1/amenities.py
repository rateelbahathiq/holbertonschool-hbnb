from flask_restx import Namespace, Resource, fields
<<<<<<< HEAD
from flask_jwt_extended import jwt_required, get_jwt
=======
>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Amenity model for input/output
amenity_model = api.model('Amenity', {
    'id': fields.String(readonly=True, description='Amenity unique identifier'),
    'name': fields.String(required=True, description='Name of the amenity'),
<<<<<<< HEAD
    'description': fields.String(required=False, description='Description of the amenity')
})

=======
    'description': fields.String(required=False,
                                 description='Description of the amenity')
})


>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.marshal_with(amenity_model, code=201)
<<<<<<< HEAD
    @jwt_required()
    def post(self):
        """Create a new amenity (Admin only)"""
        # Check for Admin privileges
        claims = get_jwt()
        if not claims.get('is_admin'):
            api.abort(403, "Administration privileges required")

=======
    def post(self):
        """Create a new amenity"""
>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
        amenity_data = api.payload
        new_amenity = facade.create_amenity(amenity_data)
        return new_amenity, 201

    @api.marshal_list_with(amenity_model)
    def get(self):
        """Retrieve all amenities"""
        return facade.get_all_amenities()

<<<<<<< HEAD
=======

>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
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
<<<<<<< HEAD
    @jwt_required()
    def put(self, amenity_id):
        """Update amenity details (Admin only)"""
        # Check for Admin privileges
        claims = get_jwt()
        if not claims.get('is_admin'):
            api.abort(403, "Administration privileges required")

=======
    def put(self, amenity_id):
        """Update amenity details"""
>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
        amenity_data = api.payload
        updated_amenity = facade.update_amenity(amenity_id, amenity_data)
        if not updated_amenity:
            return {'error': 'Amenity not found'}, 404
        return updated_amenity
