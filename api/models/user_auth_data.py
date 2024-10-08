import base
import sqlalchemy as sa


class UserAuthData(base.Base, base.RecordTimestaps):
    __tablename__ = "user_auth_data"

    user_id = sa.Column(
        sa.String,
        nullable=False,
        primary_key=True,
    )
    name = sa.Column(sa.String, nullable=False, unique=True)
    email = sa.Column(sa.String, nullable=False, unique=True)

    is_validated = sa.Column(
        sa.Boolean, nullable=False, default=False, server_default=False
    )
    password_hash = sa.Column(sa.String, nullable=False)

    user = sa.orm.relationship("User", back_populates="auth_data")
