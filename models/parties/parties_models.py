
from sqlalchemy import Column, Integer, String
from models import Base


class Parties(Base):
    __tablename__ = "parties"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String,)
    last_name = Column(String)
    age = Column(Integer)
