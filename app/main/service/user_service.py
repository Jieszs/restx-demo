import uuid
import datetime

from flask import current_app

from app.main import db
from app.main.model.user import User
from typing import Dict, Tuple

from app.main.common.response_builder import internal_err_resp, err_resp, success_data


def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        return err_resp(False, 'User already exists. Please Log in.', 409)


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def generate_token(user: User) -> Tuple[Dict[str, str], int]:
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        return success_data('Successfully registered.', {'Authorization': auth_token.decode()}), 201
    except Exception as e:
        current_app.logger.error(e)
        return internal_err_resp()


def save_changes(data: User) -> None:
    db.session.add(data)
    db.session.commit()
