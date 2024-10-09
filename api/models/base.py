import datetime

import pydantic
import sqlalchemy as sa
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.sql.functions as sql

Base = declarative.declarative_base()


class BaseModel(pydantic.BaseModel):
    class Config:
        pass


class RecordTimestaps:
    created_at = sa.Column(
        sa.TIMESTAMP,
        default=sql.func.now(),
        nullable=False,
        server_default=sql.func.now(),
    )

    updated_at = sa.Column(
        sa.TIMESTAMP,
        default=sql.func.now(),
        onupdate=sql.func.now(),
        server_default=sql.func.now(),
        nullable=False,
    )
