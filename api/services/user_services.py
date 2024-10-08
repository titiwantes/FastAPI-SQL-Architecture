import sqlalchemy as sa
import crud.user_crud
import utils
import schemas
import crud


class UserService:
    def __init__(self, dbs: tuple[sa.Session, sa.AliasSession]):
        self.reader, self.writer = dbs

    def signup(self, auth: schemas.Signup):
        existing_user = crud.UserCrud.get_user_by_email(
            db=self.reader, email=auth.email
        )
        if existing_user:
            raise ValueError("User already exists")

        password_hash = utils.hash_password(auth.password)

        user = crud.UserCrud.create(
            self.writer,
            schemas.UserCreate(),
        )

        user_auth_data = crud.UserAuthDataCrud.create(
            self.writer,
            schemas.UserAuthDataCreate(
                email=auth.email, password_hash=password_hash, id=user.id
            ),
        )

        return schemas.UserCreateOut(
            name=user.name,
            email=user_auth_data.email,
            id=user.id,
        )
