from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str          # se lee de la variable de entorno DATABASE_URL

    model_config = {"env_file": ".env",
                    "extra": "ignore"}   # y también del archivo .env

settings = Settings()