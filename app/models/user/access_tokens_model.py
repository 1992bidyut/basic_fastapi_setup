from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.ext.declarative import declared_attr
from app.models import Base


class AccessToken(Base):

    id = Column(Integer, primary_key=True, nullable=False)
    client_id = Column(String, nullable=False)
    client_secret = Column(String, nullable=False)
    token = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    expiry = Column(TIMESTAMP(timezone=True), nullable=False)

    __tablename__ = 'access_tokens'
