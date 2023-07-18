from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    API_VERSION : str = '/v1'

    DATABASE_URL :str

    class Config:
        case_sensitive = True
        env_file = os.path.abspath("app/.env")

settings = Settings()