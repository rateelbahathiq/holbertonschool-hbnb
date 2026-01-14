from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Define the user model for input (what we expect from the client)
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First Name'),
    'last_name': fields.String(required=True, description='Last Name'),
    'email': fields.String(required=True, description='Email'),
    'password': fields.String(required=True, description='Password'),
    'is_admin': fields.Boolean(description='Admin status', default=False)
})

# Define the user model for output (what we send back - NO PASSWORD)
user_output_model = api.model('UserOutput', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First Name'),
    'last_name': fields.String(description='Last Name'),
    'email': fields.String(description='Email'),
    'is_admin': fields.Boolean(description='Admin status')
})


@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.marshal_with(user_output_model, code=201)
    def post(self):
        """Create a new user"""
        user_data = api.payload

        # Check if email already exists
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return new_user, 201

    @api.marshal_list_with(user_output_model)
    def get(self):
        """Retrieve a list of all users"""
        return facade.user_repo.get_all()


@api.route('/<user_id>')
class UserResource(Resource):
    @api.marshal_with(user_output_model)
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return user

    @api.expect(user_model)
    @api.marshal_with(user_output_model)
    def put(self, user_id):
        """Update user details"""
        user_data = api.payload
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        # Update user logic (in real app, handle password hashing)
        user.update(user_data)
        return user
