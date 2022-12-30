from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import declared_attr

from app.models import Base


class PartiesAddress(Base):
    id = Column(Integer, primary_key=True, index=True)
    village = Column(String,)
    bazzar = Column(String,)
    thana = Column(String)
    district = Column(String)
    division = Column(String)

    is_active = Column(Boolean, nullable=True, default=True)
    is_deleted = Column(Boolean, nullable=True, default=False)
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))

    __tablename__ = "parties_address"
