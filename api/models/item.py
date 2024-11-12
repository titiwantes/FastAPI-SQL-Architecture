import sqlalchemy as sa
import sqlalchemy.dialects.mysql as mysql

import api.models.base as base


class Item(base.Base, base.RecordTimestamps):

    __tablename__ = "items"
    id = sa.Column(
        mysql.BIGINT(unsigned=True),
        primary_key=True,
        nullable=False,
        autoincrement=True,
    )

    name = sa.Column(
        sa.String(255),
        nullable=False,
    )

    description = sa.Column(
        sa.Text,
        nullable=True,
    )
