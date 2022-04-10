from typing import Optional
from pydantic import BaseModel, EmailStr

# from app.models.domain.users import User
# from app.models.schemas.rwschema import RWSchema


class UserInLogin(RWSchema):
    email: EmailStr
    username : str
    password: str

class UserInCreate(UserInLogin):
    username: str

class UserInUpdate(BaseModel):
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
    
    
class UserWithToken(User):
    token: str

class UserInResponse(RWSchema):
    user: UserWithToken
