class Paiement(BaseModel, Base):
    __tablename__ = "paiements"
    date_paiement = Column(DateTime)
    montant = Column(Integer)
    moyen_paiement = Column(String(30))
    id_contrat = Column(Integer, ForeignKey('contrats.id'))