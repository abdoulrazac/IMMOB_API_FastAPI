class Paiement(BaseModel, Base):
    __tablename__ = "paiements"
    date_paiement = Column(DateTime)
    montant = Column(Integer)
    moyen_paiement = Column(String(30))
    id_contrat = Column(Integer, ForeignKey('contrats.id'))

    def dict(self):
        return {
            "date_paiement": self.date_paiement,
            "montant": self.montant,
            "moyen_paiment": self.moyen_paiement,
        }