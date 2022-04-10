from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from Base import ClasseBase as Base

import datetime 

class Log(Base):
    __tablename__  = "logs"
    tentative_connexion=Column(DateTime)
    id_user = Column(Integer, ForeignKey('users.id'))