import sqlalchemy as sa

import api.models.user_auth_data as uad_mdl
import api.schemas.user_auth_data_schema as uad_sch


class UserAuthDataCrud:
    @classmethod
    def create(
        cls, db: sa.orm.Session, user_auth_data: uad_sch.UserAuthDataCreate
    ) -> uad_mdl.UserAuthData:
        try:
            user_auth_data = uad_mdl.UserAuthData(**user_auth_data.model_dump())
            db.add(user_auth_data)
            db.commit()
            db.refresh(user_auth_data)
            return user_auth_data
        except Exception as e:
            db.rollback()
            raise e
