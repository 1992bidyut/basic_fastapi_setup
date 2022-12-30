from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    postgres_hostname: str
    postgres_port: str
    postgres_db: str
    postgres_user: str
    postgres_password: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    jwt_expire_minutes: int
    client_id: str
    client_secret: str
    domain_name: str

    NO_AUTH_REQUIRED: List[str] = [
        '/',
        '/login',
    ]
    PROJECT_NAME: str = 'PMPS Backend'
    VERSION: str = '1.0.0'
    FRONTEND_HOST = 'http://pmps.zeroloop.xyz/'

    class Config:
        env_file = ".env"


settings = Settings()

