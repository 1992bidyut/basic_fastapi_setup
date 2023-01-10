
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.root.database import get_db
from app.models.user.users_model import User
from app.service import oauth2

from app.models.parties.parties_models import Parties
from app.schema.parties.parties import PartyOutSchema, PartyCreateSchema

api_router = APIRouter(
    tags=['parties']
)
auth_handler = oauth2.Auth()


@api_router.post("/profile/", response_model=PartyOutSchema)
def create_party(party_data: PartyCreateSchema, db: Session = Depends(get_db), current_user: User = Depends(auth_handler.get_current_user)):
    new = Parties(**party_data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


