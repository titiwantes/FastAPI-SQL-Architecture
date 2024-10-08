import fastapi
import schemas
import services
import db.sessions as db

router = fastapi.APIRouter()


@router.post("/users/signup")
def signup(
    user: schemas.Signup,
    db=fastapi.Depends(db.get_dbs),
):
    pass
