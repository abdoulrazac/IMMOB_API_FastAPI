from typing import Optional
from pydantic import BaseModel, EmailStr

from SchemasBase import SchemasModel

# from app.models.domain.users import User
# from app.models.schemas.rwschema import RWSchema

class UserInLogin(SchemasModel):
    email: EmailStr
    username : Optional[str]
    password: str

class UserInCreate(UserInLogin):
    user_id: int
    username: str
    email: Optional[EmailStr] = None
    password: str
    nom: str
    prenom: str
    tel: Optional[str] = None
    typeUser: int
    DoB: int
    trash: bool

class UserInUpdate(BaseModel):
    id: int
    user_name: str
    password: str
    nom: str
    prenom: str
    tel: Optional[str]
    user_type: int
    date_naissance: int
    trash: bool
    email: str
    salt: str
    
class UserWithToken(User): #####################
    token: str

class UserInResponse(SchemasModel):
    user: UserWithToken
