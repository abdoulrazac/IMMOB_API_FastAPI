from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from Base import BaseModel

Base = declarative_base()

class Client(BaseModel, Base):
    __tablename__ = "clients"
    nom = Column(String(30))
    prenom = Column(String(30))
    date_naissance = Column(DateTime)
    profession = Column(String(30))
    CNI = Column(Integer)
    email = Column(String(70)) 
    tel = Column(Integer)