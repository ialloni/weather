from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"


class Settings(BaseSettings):
    WEATHER_API_KEY: str
    CHECK_IP_URL: str
    CHECK_CITY_URL: str
    CHECK_WEATHER_URL: str

    model_config = SettingsConfigDict(env_file=ENV_PATH)


settings = Settings()  # type: ignore
