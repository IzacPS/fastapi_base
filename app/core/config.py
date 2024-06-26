from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    # PROJECT_NAME: str
    # VERSION: str = "1.0.0"

    class Config:
        env_file = ".env"


settings = Settings()
