import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    db_echo: bool
    
    @property
    def database_url_async(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property
    def database_url_sync(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    


settings = Settings(
    DB_HOST=os.getenv('DB_HOST'),
    DB_PORT=os.getenv('DB_PORT'),
    DB_USER=os.getenv('DB_USER'),
    DB_PASS=os.getenv('DB_PASS'),
    DB_NAME=os.getenv('DB_NAME'),
    db_echo=os.getenv("db_echo")
)
