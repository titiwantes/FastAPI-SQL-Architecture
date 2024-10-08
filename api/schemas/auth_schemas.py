from models import BaseModel


class Login(BaseModel):
    email: str
    name: str


class Signup(BaseModel):
    email: str
    name: str
    password: str
    password_confirm: str
