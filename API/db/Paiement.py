from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from Base import BaseModel

Base = declarative_base()

class Paiement(BaseModel, Base):
    __tablename__ = "paiements"
    date_paiement = Column(DateTime)
    montant = Column(Integer)
    moyen_paiement = Column(String(30))
    id_contrat = Column(Integer, ForeignKey('contrats.id'))