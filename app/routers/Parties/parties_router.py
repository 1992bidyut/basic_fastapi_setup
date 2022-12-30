
from fastapi import status, HTTPException, Depends, APIRouter, Request
# database engine session
from sqlalchemy.orm import Session
from app.root.database import get_db

from app.models.parties.parties_models import Parties
from app.schema.parties import PartyOut, PartyCreate, PartyUpdate

api_router = APIRouter(
    tags=['parties']
)


@api_router.post("/", response_model=PartyOut)
def create_party(party_data: PartyCreate, db: Session = Depends(get_db)):
    new = Parties(**party_data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


