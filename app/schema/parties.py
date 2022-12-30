from pydantic import BaseModel


class PartyCreate(BaseModel):
    first_name: str
    last_name: str
    age: int

    class Config:
        orm_mode = True


class PartyOut(BaseModel):
    first_name: str
    last_name: str
    age: int

    class Config:
        orm_mode = True


class PartyUpdate(BaseModel):
    first_name: str
    last_name: str
    age: int

    class Config:
        orm_mode = True


