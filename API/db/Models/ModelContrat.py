class Contrat(BaseModel, Base):
    __tablename__ = "contrats"
    debut = Column(DateTime)
    fin = Column(DateTime)
    loyer = Column(Integer)
    caution = Column(Integer)
    justificatif = Column(String(30))
    id_appartement = Column(Integer, ForeignKey('appartements.id'))
    id_client = Column(Integer, ForeignKey('clients.id'))

    # Ne pas entrer un attribut pour les clefs étrangères.
    def dict(self):
        return {
            "debut": self.debut,
            "fin": self.fin,
            "loyer": self.loyer,
            "caution": self.caution,
            "justificatif": self.justificatif
        }