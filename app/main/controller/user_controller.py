from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from .schemas.user import UserSchema
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user
from typing import Dict, Tuple

from app.main.common.response_builder import message

api = UserDto.api
_user = UserDto.user
parser = api.parser()
parser.add_argument('Authorization', location='headers')


@api.route('/')
@api.expect(parser)
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @admin_token_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    def get(self, public_id):
        """get a user given its identifier"""
        schema = UserSchema()
        user = get_a_user(public_id)
        if not user:
            return message(False, 'User not found.'), 404
        else:
            return schema.dump(user)
