from pydantic_settings import BaseSettings
from pydantic import Field, AnyUrl, field_validator
from typing import Any


class DatabaseSettings(BaseSettings):
    DB_PORT: int  # = Field(5432)
    DB_NAME: str  # = Field("mysql")
    DB_USER: str  # = Field("user")
    DB_HOST: str  # = Field("localhost")
    DB_PASSWORD: str  # = Field("password")
    DB_URL: AnyUrl | None

    @field_validator("DB_URL", pre=True)
    def assemble_db_connection(cls, v: str | None, values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return AnyUrl.build(
            scheme="mysql+pymysql",
            user=values.get("DB_USER"),
            password=values.get("DB_PASSWORD"),
            host=values.get("DB_HOST"),
            port=values.get("DB_PORT"),
            path=f"/{values.get('DB_NAME') or ''}",
        )


class Settings(DatabaseSettings):
    DEBUG: bool = False


settings = Settings()
