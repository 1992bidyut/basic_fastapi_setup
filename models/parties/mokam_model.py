
from sqlalchemy import Column, Integer, String
from models import Base


class Mokam(Base):
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String,)
    village = Column(String,)
    bazzar = Column(String,)
    thana = Column(String)
    district = Column(String)
    division = Column(String)

    __tablename__ = "mokam"
