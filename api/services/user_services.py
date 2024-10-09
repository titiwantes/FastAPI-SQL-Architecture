import sqlalchemy as sa

import api.crud.user_auth_data_crud as uad_crud
import api.crud.user_crud as user_crud
import api.schemas.auth_schemas as auth_sch
import api.schemas.user_auth_data_schema as uad_sch
import api.schemas.user_schemas as user_sch
import api.utils.security as security


class UserService:
    def __init__(self, dbs: tuple[sa.orm.Session, sa.orm.Session]):
        self.reader, self.writer = dbs

    def signup(self, auth: auth_sch.Signup):
        existing_user = user_crud.UserCrud.get_user_by_email(
            db=self.reader, email=auth.email
        )
        if existing_user:
            raise ValueError("User already exists")

        password_hash = security.hash_password(auth.password)

        user = user_crud.UserCrud.create(
            self.writer,
            user_sch.UserCreate(),
        )

        user_auth_data = uad_crud.UserAuthDataCrud.create(
            self.writer,
            uad_sch.UserAuthDataCreate(
                email=auth.email,
                password_hash=password_hash,
                user_id=user.id,
                name=auth.name,
            ),
        )

        return user_sch.UserCreateOut(
            name=user_auth_data.name,
            email=user_auth_data.email,
            id=user.id,
        )
