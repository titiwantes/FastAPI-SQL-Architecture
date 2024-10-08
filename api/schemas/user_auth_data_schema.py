import models
import uuid


class UserAuthDataCreate(models.BaseModel):
    id: str
    email: str
    name: str
    password_hash: str
