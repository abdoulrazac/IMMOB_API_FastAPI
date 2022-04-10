from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from Base import ClasseBase as Base

import datetime 



class Client(Base):
    __tablename__ = "clients"
    nom = Column(String(30))
    prenom = Column(String(30))
    date_naissance = Column(DateTime)
    profession = Column(String(30))
    CNI = Column(Integer)
    email = Column(String(70)) 
    tel = Column(Integer(10))