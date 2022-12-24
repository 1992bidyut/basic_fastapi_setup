from pydantic import BaseModel


class Parties(BaseModel):
    first_name: str
    last_name: str
    age: int

    class Config:
        orm_mode = True


