from flask import current_app

from app.main.model.user import User
from ..service.blacklist_service import save_token
from typing import Dict, Tuple

from app.main.common.response_builder import success_data, message, internal_err_resp


class Auth:

    @staticmethod
    def login_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = User.encode_auth_token(user.id)
                if auth_token:
                    return success_data('Successfully logged in.', {'Authorization': auth_token.decode()})
            else:
                return message(False, 'email or password does not match.'), 401

        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def logout_user(data: str) -> Tuple[Dict[str, str], int]:
        auth_token = data
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                return message(False, resp), 401
        else:
            return message(False, 'Provide a valid auth token.'), 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                data = {
                    'user_id': user.id,
                    'email': user.email,
                    'admin': user.admin,
                    'registered_on': str(user.registered_on)
                }
                return success_data('logged in success', data), 200
            return message(False, resp), 401
        else:
            return message(False, 'Provide a valid auth token.'), 401
