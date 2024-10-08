import sqlalchemy as sa
import schemas
import models


class UserAuthDataCrud:
    def __init__(self, dbs: tuple[sa.Session, sa.AliasSession]):
        self.reader, self.writer = dbs

    def create(self, user_auth_data: schemas.UserAuthDataCreate) -> models.UserAuthData:
        try:
            user_auth_data = models.UserAuthData(**user_auth_data.model_dump())
            self.writer.add(user_auth_data)
            self.writer.commit()
            self.writer.refresh(user_auth_data)
            return user_auth_data
        except Exception as e:
            self.writer.rollback()
            raise e
