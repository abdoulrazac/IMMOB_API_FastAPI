from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from Base import ClasseBase as Base

import datetime 

class Contrat(Base):
    __tablename__ = "contrats"
    debut = Column(DateTime)
    fin = Column(DateTime)
    loyer = Column(Integer)
    caution = Column(Integer)
    justificatif = Column(String(30))
    id_appartement = Column(Integer, ForeignKey('appartements.id'))
    id_client = Column(Integer, ForeignKey('clients.id'))