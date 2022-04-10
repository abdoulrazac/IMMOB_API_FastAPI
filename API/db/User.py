from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from Base import BaseModel

Base = declarative_base()

class User(BaseModel, Base):
    __tablename__ = "users"
    user_name = Column(String(30))
    password = Column(String(30))
    nom = Column(String(30))
    prenom = Column(String(30))
    tel = Column(Integer)
    user_type = Column(Boolean)
    date_naissance = Column(DateTime)
    trash = Column(Boolean)
    email = Column(String(70)) 