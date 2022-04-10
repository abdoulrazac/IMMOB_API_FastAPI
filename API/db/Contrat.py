from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from Base import BaseModel

Base = declarative_base()

class Contrat(BaseModel, Base):
    __tablename__ = "contrats"
    debut = Column(DateTime)
    fin = Column(DateTime)
    loyer = Column(Integer)
    caution = Column(Integer)
    justificatif = Column(String(30))
    id_appartement = Column(Integer, ForeignKey('appartements.id'))
    id_client = Column(Integer, ForeignKey('clients.id'))