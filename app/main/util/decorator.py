from functools import wraps

from flask import request

from app.main.service.auth_helper import Auth
from typing import Callable

from app.main.common.response_builder import message


def token_required(f) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated


def admin_token_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        admin = token.get('admin')
        if not admin:
            return message(False, 'admin token required'), 401

        return f(*args, **kwargs)

    return decorated
