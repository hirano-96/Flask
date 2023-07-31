from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config') 
jwt = JWTManager(app)

import controllers.views
