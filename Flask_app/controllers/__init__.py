from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config') 
jwt = JWTManager(app)
api = Api(app, doc='/documents/')

import controllers.secure