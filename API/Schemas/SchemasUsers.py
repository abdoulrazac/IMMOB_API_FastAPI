import datetime
from typing import Optional, DateTime
from pydantic import BaseModel, EmailStr

from API.Schemas.SchemasBase import SchemasModel

# from app.models.domain.users import User
# from app.models.schemas.rwschema import RWSchema

class User(SchemasModel):
    username: str

class UserInLogin(BaseModel):
    email: Optional[EmailStr]
    username : Optional[str]
    password: str

class UserInUpdate(BaseModel):
    id: int
    nom: str
    prenom: str
    tel: Optional[str]
    date_naissance: datetime.datetime
    email: str

class UserInCreate(UserInUpdate):
    username: str
    email: Optional[EmailStr] = None
    password: str
    password_valid: str
    typeUser: int
    trash: bool = False

class UserInDb(UserInUpdate):
    username: str
    email: Optional[EmailStr] = None
    password: str
    typeUser: int
    trash: bool = False

class UserWithToken(User):
    token: str

class UserInResponse(SchemasModel):
    user: UserWithToken