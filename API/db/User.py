from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from Base import ClasseBase as Base

import datetime 

class User(Base):
    __tablename__ = "users"
    user_name = Column(String(30))
    password = Column(String(30))
    nom = Column(String(30))
    prenom = Column(String(30))
    tel = Column(Integer(10))
    user_type = Column(bool)
    date_naissance = Column(DateTime)
    trash = Column(bool)
    email = Column(String(70)) 