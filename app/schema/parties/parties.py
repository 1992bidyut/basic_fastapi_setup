from pydantic import BaseModel


class PartyCreateSchema(BaseModel):
    first_name: str
    last_name: str
    age: int

    class Config:
        orm_mode = True


class PartyOutSchema(BaseModel):
    first_name: str
    last_name: str
    age: int

    class Config:
        orm_mode = True


class PartyUpdateSchema(BaseModel):
    first_name: str
    last_name: str
    age: int

    class Config:
        orm_mode = True


