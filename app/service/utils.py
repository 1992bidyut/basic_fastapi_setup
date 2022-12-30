import json
import os

from app.models.user.access_tokens_model import AccessToken
import datetime
from app.root.configs import settings
import secrets
import math, operator
from sqlalchemy.sql import operators
from sqlalchemy import orm
from app.root.database import get_session
import decimal

ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(client_data, db):
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = secrets.token_urlsafe()
    client_data.expiry = expire
    client_data.token = token
    access_token = AccessToken(**client_data.dict())
    db.add(access_token)
    db.commit()
    db.refresh(access_token)
    return access_token


class ExtendedEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

