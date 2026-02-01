from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

<<<<<<< HEAD
# Define the user model for input
=======
# Define the user model for input (what we expect from the client)
>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First Name'),
    'last_name': fields.String(required=True, description='Last Name'),
    'email': fields.String(required=True, description='Email'),
    'password': fields.String(required=True, description='Password'),
    'is_admin': fields.Boolean(description='Admin status', default=False)
})

<<<<<<< HEAD
=======
# Define the user model for output (what we send back - NO PASSWORD)
>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
user_output_model = api.model('UserOutput', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First Name'),
    'last_name': fields.String(description='Last Name'),
    'email': fields.String(description='Email'),
<<<<<<< HEAD
    'is_admin': fields.Boolean(description='Admin status'),
    # Never return the password!
})

@api.route('/')
class UserList(Resource):
    @api.doc('create_user')
    @api.expect(user_model)
    @api.marshal_with(user_output_model, code=201)
    def post(self):
        """Register a new user"""
        user_data = api.payload
        
        # Check if user already exists
        user = facade.get_user_by_email(user_data['email'])
        if user:
            api.abort(400, "User already exists")
            
        # Create new user (The Model handles the hashing now!)
        new_user = facade.create_user(user_data)
        
        return new_user, 201

@api.route('/<user_id>')
class UserResource(Resource):
    @api.doc('get_user')
=======
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
>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
    @api.marshal_with(user_output_model)
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
<<<<<<< HEAD
            api.abort(404, "User not found")
=======
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
        user_data.pop('password', None)

        user.update(user_data)
>>>>>>> 52e00562050634211fed8dceba1bc0a709fb72e8
        return user
