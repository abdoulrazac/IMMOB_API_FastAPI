from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from Base import BaseModel

Base = declarative_base()

class Log(BaseModel, Base):
    __tablename__  = "logs"
    tentative_connexion=Column(DateTime)
    id_user = Column(Integer, ForeignKey('users.id'))