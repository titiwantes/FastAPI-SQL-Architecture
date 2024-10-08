import datetime

import pydantic
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(pydantic.BaseModel):
    class Config:
        pass


class RecordTimestaps:
    created_at = sqlalchemy.Column(
        sqlalchemy.TIMESTAMP,
        default=datetime.datetime.now(),
        nullable=False,
        server_default=sqlalchemy.func.now(),
    )

    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now(),
        server_default=sqlalchemy.func.now(),
        nullable=False,
    )
