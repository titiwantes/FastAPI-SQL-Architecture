import fastapi

import api.schemas.auth_schemas as auth_sch
import api.services.user_services as user_srv
import db.sessions as db

router = fastapi.APIRouter()


@router.post("/users/signup")
def signup(
    user: auth_sch.Signup,
    dbs=fastapi.Depends(db.get_dbs),
):
    user_service = user_srv.UserService(dbs=dbs)
    result = user_service.signup(user)

    return result
