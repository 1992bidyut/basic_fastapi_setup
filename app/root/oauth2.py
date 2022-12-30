from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.user import users_model, access_tokens_model
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.root.configs import settings
from app.root.database import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


class Auth():
    hasher = CryptContext(schemes=['bcrypt'], deprecated="auto")
    secret = settings.secret_key
    algorithm = settings.algorithm
    jwt_expire_minutes = settings.jwt_expire_minutes
    jwt_refresh_expire_hours = 10

    def encode_password(self, password):
        return self.hasher.hash(password)

    def verify_password(self, password, encoded_password):
        return self.hasher.verify(password, encoded_password)

    def encode_token(self, payload_data: dict):
        payload = {
            'exp': datetime.utcnow() + timedelta(minutes=self.jwt_expire_minutes),
            'iat': datetime.utcnow(),
            'scope': 'access_token',
            'data': payload_data
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm=self.algorithm
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            if payload['scope'] == 'access_token':
                return payload['data']
            raise HTTPException(status_code=401, detail='Scope for the token is invalid')
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token expired')
        except JWTError:
            raise HTTPException(status_code=401, detail='Invalid token')

    def encode_refresh_token(self, payload_data: dict):
        payload = {
            'exp': datetime.utcnow() + timedelta(hours=self.jwt_refresh_expire_hours),
            'iat': datetime.utcnow(),
            'scope': 'refresh_token',
            'data': payload_data
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm=self.algorithm
        )

    def refresh_token(self, refresh_token):
        try:
            payload = jwt.decode(refresh_token, self.secret, algorithms=[self.algorithm])
            if payload['scope'] == 'refresh_token':
                data = payload['data']
                new_token = self.encode_token(data)
                return new_token
            raise HTTPException(status_code=401, detail='Invalid scope for token')
        except JWTError:
            raise HTTPException(status_code=401, detail='Invalid refresh token')

    def get_current_user(self, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
        token = self.decode_token(token)
        user = db.query(users_model.User).filter(users_model.User.id == token['user_id']).first()

        return user

    def valid_access_token(self, token: str, db: Session):
        access_token = db.query(access_tokens_model.AccessToken).filter(access_tokens_model.AccessToken.token == token).first()
        if access_token and access_token.expiry.replace(tzinfo=None) > datetime.utcnow():
            return True
        return False

