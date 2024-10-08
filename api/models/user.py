import base
import sqlalchemy as sa


class User(base.Base, base.RecordTimestaps):
    __tablename__ = "users"

    id = sa.Column(
        sa.String,
        primary_key=True,
        nullable=False,
        default=sa.func.uuid(),
        server_default=sa.func.uuid(),
    )

    auth_data = sa.orm.relationship("UserAuthData", back_populates="user")
