from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Task Manager API"
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost:5432/taskdb"

    class Config:
        env_file = ".env"

settings = Settings()