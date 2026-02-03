from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import create_access_token

api = Namespace('auth', description='Authentication operations')

login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Login user"""
        data = api.payload
        email = data.get('email')
        password = data.get('password')

        user = facade.get_user_by_email(email)
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}, 200
        
        return {'message': 'Invalid credentials'}, 401
