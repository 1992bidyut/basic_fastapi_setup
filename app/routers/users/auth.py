from fastapi import APIRouter, Depends, status, HTTPException, Header
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer

# from app.models.user.user_menu import UserMenu
from app.root import configs, database
from app.service import utils, oauth2
from app.schema.users.access_tokens import AccessTokenCreateSchema, AccessTokenOutSchema, Token
from app.models.user.users_model import User
from app.schema.users.users import UserLoginSchema

settings = configs.settings

api_router = APIRouter(tags=['Authentication'])

auth_handler = oauth2.Auth()
security = HTTPBearer()


@api_router.post('/accesstoken', response_model=AccessTokenOutSchema, name='auth:accesstoken')
def access_token(client_data: AccessTokenCreateSchema, db: Session = Depends(database.get_db)):
    client_id = settings.client_id
    client_secret = settings.client_secret
    print(f"Settings ID: {client_id} and Request ID={client_data.client_id}")
    print(f"Settings Secret: {client_secret} and Request Secret={client_data.client_secret}")
    if client_id == client_data.client_id and client_secret == client_data.client_secret:
        try:
            token = utils.create_access_token(client_data=client_data, db=db)
            return {'token': token.token}
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Access Token Creation Failed")

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Client ID and Secret Doesn't Match")


@api_router.post('/login', response_model=Token, name='auth:login')
def login(user_credentials: UserLoginSchema, db: Session = Depends(database.get_db), accesstoken: str = Header(None)):
    if auth_handler.valid_access_token(accesstoken, db):
        user = db.query(User).filter(
            User.email == user_credentials.username).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

        if not auth_handler.verify_password(user_credentials.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

        # user_menu = db.query(UserMenu).filter(UserMenu.user_id == user.id).first()
        #
        # if user_menu:
        #     menu = user_menu.menu
        # else:
        #     menu = utils.import_base_menu(user.user_type)

        token = auth_handler.encode_token(
            {
                "user_id": user.id,
                "user_type": user.user_type,
                "username": user.email,
                # "user_type_text": user.user_type_text,
                # "menu": menu
            }
        )

        ref_token = auth_handler.encode_refresh_token(
            {
                "user_id": user.id,
                "user_type": user.user_type,
                "username": user.email,
                # "user_type_text": user.user_type_text,
                # "menu": menu
            }
        )

        return {"access_token": token, "token_type": "bearer", "refresh_token": ref_token}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Access Token")


@api_router.post('/refresh_token')
def refresh_token(data: dict):
    token = data.get('refreshtoken')
    new_token = auth_handler.refresh_token(token)
    return {'access_token': new_token}
