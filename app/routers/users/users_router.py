from fastapi import Depends, HTTPException, status, APIRouter, Header
from app.service import oauth2
from app.root.database import get_db
from sqlalchemy.orm import Session
from app.service.enums import E_UserType

from app.models.user.users_model import User
from app.schema.users.users import UserCreateSchema, UserOutSchema

api_router = APIRouter(
    tags=['users']
)
auth_handler = oauth2.Auth()


@api_router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOutSchema, name="users:create-user")
def create_user(user: UserCreateSchema, db: Session = Depends(get_db), accesstoken: str = Header(None)):
    # hash the password - user.password
    if auth_handler.valid_access_token(accesstoken, db):
        hashed_password = auth_handler.encode_password(user.password)
        user.password = hashed_password
        user_data = user.dict()
        party_id = user_data.pop('party_id') if 'party_id' in user_data else ''
        if user.user_type != E_UserType.Admin.value and not party_id:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='No {} tagged with this user!'.format(E_UserType(user.user_type).name)
            )
        new_user = User(**user_data)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        db.close()

        # if user.user_type != E_UserType.Admin.value and party_id:
        #     party_user_data = {'party_id': party_id, 'user_id': new_user.id}
        #     party_user = PartyUser(**party_user_data)
        #     db.add(party_user)
        #     db.commit()
        #     db.refresh(party_user)
        #     db.close()

        return new_user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Access Token")
