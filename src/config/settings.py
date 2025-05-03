from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Define your settings here
    bot_token: SecretStr  # Use SecretStr for sensitive values

    class Config:
        # Load from a .env file (default)
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Ignore extra fields from .env
