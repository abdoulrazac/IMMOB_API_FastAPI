from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl

from app.models.domain.users import User
from app.models.schemas.rwschema import RWSchema


class UserInLogin(RWSchema):
    email: EmailStr
    password: str

class UserInCreate(UserInLogin):
    username: str

class UserInUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    nom: Optional[str] = None
    prenom: Optional[str] = None
    tel: Optional[str] = None
    typeUser: Optional[str] = None
    DoB: Optional[str] = None
    trash: Optional[str] = None
    
    
class UserWithToken(User):
    token: str

class UserInResponse(RWSchema):
    user: UserWithToken
