from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

import datetime 

Base = declarative_base()

class ClasseBase(Base):
    id = Column(Integer, primary_key=True)
    create_at  = Column(DateTime, default = datetime.datetime.utcnow)
    update_at  = Column(DateTime, default = datetime.datetime.utcnow)


class User(ClasseBase):
    __tablename__ = "users"
    user_name = Column(String(30))
    password = Column(String(30))
    nom = Column(String(30))
    prenom = Column(String(30))
    tel = Column(Int(10))
    user_type = Column(bool)
    date_naissance = Column(Date)
    trash = Column(bool)
    email = Column(String(70)) 


class Client(ClasseBase):
    __tablename__ = "clients"
    nom = Column(String(30))
    prenom = Column(String(30))
    date_naissance = Column(Date)
    profession = Column(String(30))
    CNI = Column(Integer)
    email = Column(String(70)) 
    tel = Column(Int(10))