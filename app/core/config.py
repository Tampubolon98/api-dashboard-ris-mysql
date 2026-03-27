from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    # Optional: Construct the database URL for convenience
    @property
    def DATABASE_URL(self) -> str:
        # Format the URL for SQLAlchemy (e.g., mysql+pymysql://user:password@host:port/dbname)
        return f"mysql+pymysql://{self.DB_USER}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(case_sensitive=True)

settings = Settings()
