"""Application configuration."""
from pydantic import BaseSettings
from pydantic import Field


def get_settings() -> BaseSettings:
    """Get application settings."""

    class Settings(BaseSettings):  # pylint: disable=too-few-public-methods
        """Application settings."""

        db_url: str = Field(..., env="DATABASE_URL")
        db_engine_pool_size: int = Field(19, env="DATABASE_ENGINE_POOL_SIZE")
        db_engine_max_overflow: int = Field(0, env="DATABASE_ENGINE_MAX_OVERFLOW")
        telegram_chat_id: str = Field(..., env="TELEGRAM_CHAT_ID")
        telegram_token: str = Field(..., env="TELEGRAM_TOKEN")

    application_settings = Settings()

    # Required for postgres Heroku deprecated postgres naming
    application_settings.db_url = application_settings.db_url.replace(
        "postgres://", "postgresql://", 1
    )

    return application_settings


settings = get_settings()
