from typing import List, Optional

from pydantic import BaseModel, Field
from SchemasBase import SchemasModel

# from app.models.domain.appartements import Appartement
# from app.models.schemas.rwschema import RWSchema

DEFAULT_ARTICLES_LIMIT = 20
DEFAULT_ARTICLES_OFFSET = 0


class AppartementForResponse(SchemasModel, Appartement):
    tags: List[str] = Field(..., alias="tagList")


class AppartementInResponse(SchemasModel):
    appartement: AppartementForResponse


class AppartementInCreate(SchemasModel):
    adress: str
    ville: str
    taille: int
    nb_chambre : int
    prix: int
    loyer_min: int
    disponible : bool


class AppartementInUpdate(SchemasModel):
    adress: str
    ville: str
    taille: int
    nb_chambre : int
    description: str
    loyer_min: str
    libre : bool


class ListOfAppartementsInResponse(SchemasModel):
    appartements: List[AppartementForResponse]
    appartements_count: int


class AppartementsFilters(BaseModel):
    tag: Optional[str] = None
    author: Optional[str] = None
    favorited: Optional[str] = None
    limit: int = Field(DEFAULT_ARTICLES_LIMIT, ge=1)
    offset: int = Field(DEFAULT_ARTICLES_OFFSET, ge=0)