from typing import Optional

import models.base as base


class UserCreate(base.BaseModel):
    pass


class UserCreateOut(base.BaseModel):
    id: str
    email: str
    name: str


class UserUpdate(base.BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
