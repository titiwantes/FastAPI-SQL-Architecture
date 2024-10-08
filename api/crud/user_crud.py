import models
import sqlalchemy as sa
import schemas


class UserCrud:

    @classmethod
    def get_user_by_email(cls, db: sa.orm.Session, email: str) -> models.User:
        try:
            user = (
                db.query(models.User).filter(models.UserAuthData.email == email).first()
            )
            return user
        except Exception as e:
            raise e

    def create(cls, user: schemas.UserCreate) -> models.User:
        try:
            user = models.User(**user.model_dump())
            cls.db.add(user)
            cls.db.commit()
            cls.db.refresh(user)
            return user
        except Exception as e:
            cls.db.rollback()
            raise e
