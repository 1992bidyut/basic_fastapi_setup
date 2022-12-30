
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from app.root.configs import settings
import os


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_hostname}:{settings.postgres_port}/{settings.postgres_db}'


TEST_DATABASE_URL = f"{SQLALCHEMY_DATABASE_URL}_test"

engine = create_engine(TEST_DATABASE_URL if os.getenv('TESTING') else SQLALCHEMY_DATABASE_URL, pool_size=50, max_overflow=0)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

# Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_session():
    return scoped_session(SessionLocal)
