class Appartement(BaseModel, Base):
    __tablename__ = "appartements"
    adresse = Column(String(30))
    ville = Column(String(30))
    taille = Column(Integer)
    nb_chambre = Column(Integer)
    prix = Column(Integer)
    loyer_min = Column(Integer) 
    disponible = Column(Boolean)
    