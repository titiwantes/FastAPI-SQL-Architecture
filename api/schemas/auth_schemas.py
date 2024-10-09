import api.models.base as base


class Login(base.BaseModel):
    email: str
    name: str


class Signup(base.BaseModel):
    email: str
    name: str
    password: str
    password_confirm: str
