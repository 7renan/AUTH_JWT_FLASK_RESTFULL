from flask import Flask
from src.domain.auth.auth_routes import auth_routes


# user
from .data import user

app = Flask(__name__)

app.config['debug'] = True

auth_routes.init_app(app)
