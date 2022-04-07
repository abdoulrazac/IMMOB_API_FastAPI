from typing import List, Optional

from pydantic import BaseModel, Field

# from app.models.domain.appartements import Appartement
# from app.models.schemas.rwschema import RWSchema

DEFAULT_ARTICLES_LIMIT = 20
DEFAULT_ARTICLES_OFFSET = 0


class AppartementForResponse(RWSchema, Appartement):
    tags: List[str] = Field(..., alias="tagList")


class AppartementInResponse(RWSchema):
    appartement: AppartementForResponse


class AppartementInCreate(RWSchema):
    adress: str
    ville: str
    taille: int
    nb_chambre : int
    description: str
    loyer_min: str
    libre : bool


class AppartementInUpdate(RWSchema):
    adress: str
    ville: str
    taille: int
    nb_chambre : int
    description: str
    loyer_min: str
    libre : bool


class ListOfAppartementsInResponse(RWSchema):
    appartements: List[AppartementForResponse]
    appartements_count: int


class AppartementsFilters(BaseModel):
    tag: Optional[str] = None
    author: Optional[str] = None
    favorited: Optional[str] = None
    limit: int = Field(DEFAULT_ARTICLES_LIMIT, ge=1)
    offset: int = Field(DEFAULT_ARTICLES_OFFSET, ge=0)