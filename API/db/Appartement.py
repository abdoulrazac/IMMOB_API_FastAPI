from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from Base import ClasseBase as Base

import datetime


class Appartement(Base):
    __tablename__ = "appartements"
    adresse = Column(String(30))
    ville = Column(String(30))
    taille = Column(Integer)
    nb_chambre = Column(Integer)
    prix = Column(Integer)
    loyer_min = Column(Integer) 
    disponible = Column(Boolean)
    