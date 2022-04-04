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
    title: str
    description: str
    body: str
    tags: List[str] = Field([], alias="tagList")


class AppartementInUpdate(RWSchema):
    title: Optional[str] = None
    description: Optional[str] = None
    body: Optional[str] = None


class ListOfAppartementsInResponse(RWSchema):
    appartements: List[AppartementForResponse]
    appartements_count: int


class AppartementsFilters(BaseModel):
    tag: Optional[str] = None
    author: Optional[str] = None
    favorited: Optional[str] = None
    limit: int = Field(DEFAULT_ARTICLES_LIMIT, ge=1)
    offset: int = Field(DEFAULT_ARTICLES_OFFSET, ge=0)