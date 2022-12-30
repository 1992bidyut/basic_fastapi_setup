from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from pydantic.types import conint
from typing import Optional


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None

class AccessTokenOutSchema(BaseModel):
    token: str

    class Config:
        orm_mode = True


class AccessTokenCreateSchema(BaseModel):
    client_id: str
    client_secret: str
    token: Optional[str]
    expiry: Optional[datetime]

