from flask import Blueprint, jsonify
from flask_restx import Api
from marshmallow import ValidationError

from .main.controller.auth_controller import api as auth_ns
from .main.controller.music_controller import api as music_ns
from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus (restx) web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(music_ns, path='/music')
