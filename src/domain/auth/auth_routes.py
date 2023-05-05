from flask_restful import Api

# resources
from src.domain.auth.auth_resource import Auth, VerifyUser

auth_routes = Api()
auth_routes.add_resource(Auth, '/login')
auth_routes.add_resource(VerifyUser, '/verify-token')
