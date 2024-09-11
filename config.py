from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_id: str
    api_hash: str

    bot_token: str

    db_name: str
    db_user: str
    db_password: str
    db_server: str

    class Config:
        env_file = ".env"


settings = Settings()
