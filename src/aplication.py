from flask import Flask
from src.domain.auth.auth_resource import auth_api


# user
from .data import user

app = Flask(__name__)

app.config['debug'] = True

auth_api.init_app(app)
