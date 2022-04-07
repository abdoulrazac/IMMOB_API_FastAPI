
from typing import Optional
from pydantic import BaseModel

class ClientsInUpdate(BaseModel):
    
    idClient: int
    nomClient: Optional[str] = None
    prenomClient: Optional[str] = None
    DoBClient: Optional[str] = None
    profession: Optional[str] = None
    CNI: Optional[str] = None
    emailClient: Optional[str] = None
    telClient: Optional[str] = None





# from app.models.domain.profiles import Profile

# class ProfileInResponse(BaseModel):
#     profile: Profile



# POUR SAUVER LES CHANGEMENTS :
# git add *
# git commit --m "message"
# git push