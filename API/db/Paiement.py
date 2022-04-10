from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from Base import ClasseBase as Base

import datetime 

class Paiement(Base):
    __tablename__ = "paiements"
    date_paiement = Column(DateTime)
    montant = Column(Integer)
    moyen_paiement = Column(String(30))
    id_contrat = Column(Integer, ForeignKey('contrats.id'))