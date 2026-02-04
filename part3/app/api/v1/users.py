from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email address'),
    'is_admin': fields.Boolean(description='Admin status', default=False)
})

user_create_model = api.model('UserCreate', {
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email address'),
    'password': fields.String(required=True, description='Password'),
    'is_admin': fields.Boolean(description='Admin status', default=False)
})

@api.route('/')
class UserList(Resource):
    @api.doc('create_user')
    @api.expect(user_create_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        user_data = api.payload
        if facade.get_user_by_email(user_data['email']):
            return {'message': 'Email already registered'}, 400
        user = facade.create_user(user_data)
        return user, 201

@api.route('/<user_id>')
class UserResource(Resource):
    @api.doc('get_user')
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Fetch a user given its identifier"""
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        return user

    @api.doc('update_user')
    @api.expect(user_create_model)
    @api.marshal_with(user_model)
    @jwt_required()
    def put(self, user_id):
        """Update a user"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)

        # Logic: User can only update themselves. Admins can update anyone.
        if current_user_id != user_id and not is_admin:
            return {'message': 'Unauthorized action'}, 403

        # Logic: Non-admins cannot update email or password
        user_data = api.payload
        if not is_admin:
            if 'email' in user_data or 'password' in user_data:
                return {'message': 'You cannot modify email or password'}, 400

        user = facade.update_user(user_id, user_data)
        if not user:
            api.abort(404, "User not found")
        return user
