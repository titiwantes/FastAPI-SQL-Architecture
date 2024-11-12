import sqlalchemy as sa
import sqlalchemy.dialects.mysql as mysql
import sqlalchemy.orm as orm

import api.models.base as base


class User(base.Base, base.RecordTimestamps):

    __tablename__ = "users"

    id = sa.Column(
        mysql.BIGINT(unsigned=True),
        primary_key=True,
        nullable=False,
    )

    auth_data = orm.relationship(
        "UserAuthData", back_populates="user", cascade="all, delete-orphan"
    )
