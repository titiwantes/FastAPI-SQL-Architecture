import sqlalchemy as sa
import sqlalchemy.dialects.mysql as mysql
import sqlalchemy.orm as orm

import api.models.base as base


class UserAuthData(base.Base):

    __tablename__ = "user_auth_data"
    user_id = sa.Column(
        mysql.BIGINT(unsigned=True),
        sa.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )
    email = sa.Column(sa.String(255), nullable=False, unique=True)
    name = sa.Column(sa.String(255), nullable=False, unique=True)
    password_hash = sa.Column(sa.String(255), nullable=False)
    is_validated = sa.Column(sa.Boolean, nullable=False, default=False)
    user = orm.relationship("User", back_populates="auth_data")
