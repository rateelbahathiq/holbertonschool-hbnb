from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.doc('create_amenity')
    @api.expect(amenity_model)
    @api.marshal_with(amenity_model, code=201)
    @jwt_required()
    def post(self):
        """Create a new amenity"""
        claims = get_jwt()
        # Logic: Only Admin can create amenities
        if not claims.get('is_admin'):
            return {'message': 'Admin privileges required'}, 403

        amenity = facade.create_amenity(api.payload)
        return amenity, 201

    @api.doc('list_amenities')
    @api.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        return facade.get_all_amenities()

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.doc('get_amenity')
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Fetch an amenity given its identifier"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, "Amenity not found")
        return amenity

    @api.doc('update_amenity')
    @api.expect(amenity_model)
    @api.marshal_with(amenity_model)
    @jwt_required()
    def put(self, amenity_id):
        """Update an amenity"""
        claims = get_jwt()
        # Logic: Only Admin can update amenities
        if not claims.get('is_admin'):
            return {'message': 'Admin privileges required'}, 403

        amenity = facade.update_amenity(amenity_id, api.payload)
        if not amenity:
            api.abort(404, "Amenity not found")
        return amenity
