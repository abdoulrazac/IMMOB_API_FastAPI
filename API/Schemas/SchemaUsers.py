import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, root_validator

from API.Schemas.SchemaBase import SchemasModel
# from app.models.domain.users import User
# from app.models.schemas.rwschema import RWSchema
from API.Schemas.Common import DateTimeModelMixin, IDModelMixin


class User(SchemasModel):
    username: str

class UserInLogin(BaseModel):
    email: Optional[EmailStr] = None
    username : Optional[str] = None
    password: str

    @root_validator
    def check_email_or_username(cls, values):
        if not (values.get('email') or values.get('username')):
            raise ValueError("Email ou username manquants")


class UserInUpdate(DateTimeModelMixin):
    username: str
    nom: str
    prenom: str
    email: Optional[EmailStr] = None
    tel: Optional[str]
    date_naissance: datetime.datetime


class UserInCreate(UserInUpdate):
    email: Optional[EmailStr] = None
    password1: str
    password2: str
    usertype: int
    trash: bool = False

    @root_validator
    def check_passwords_match(cls, values):
        pw1, pw2 = values.get('password1'), values.get('password2')
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('Passwords do not match')
        return values


class UserInDb(UserInUpdate, IDModelMixin):
    email: Optional[EmailStr] = None
    password: str
    usertype: int
    trash: bool = False
    salt: str

class UserWithToken(User):
    token: str

class UserInResponse(SchemasModel):
    user: UserWithToken