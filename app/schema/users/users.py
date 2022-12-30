from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional


class UserOutSchema(BaseModel):
    id: int
    email: EmailStr
    user_type: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserListSchema(BaseModel):
    limit: int
    page: int
    records: int
    total: int
    rows: List[UserOutSchema]

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str
    user_type: int
    party_id: Optional[int]


class UserLoginSchema(BaseModel):
    username: EmailStr
    password: str
