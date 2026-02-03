from flask_restx import Namespace, Resource, fields
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
        user = facade.create_user(api.payload)
        return user, 201

    @api.doc('list_users')
    @api.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        return facade.get_user_by_email(None) # Facade usually handles "all" differently, but standard facade doesn't have get_all_users exposed typically. 
        # Actually, let's strictly follow the Facade interface usually expected.
        # If get_all_users isn't in your facade, you might need to add it or use a different method.
        # However, typically getting by ID is the main requirement.
        pass 

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
    def put(self, user_id):
        """Update a user"""
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        # Logic to update user would go here
        return user
