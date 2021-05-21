from flask import current_app

from app.main import db

from app.main.model.blacklist import BlacklistToken
from typing import Dict, Tuple

from app.main.common.response_builder import success, message


def save_token(token: str) -> Tuple[Dict[str, str], int]:
    blacklist_token = BlacklistToken(token=token)
    try:
        # insert the token
        db.session.add(blacklist_token)
        db.session.commit()
        return success('Successfully logged out.')
    except Exception as e:
        current_app.logger.error(e)
        return message(False, e), 200
