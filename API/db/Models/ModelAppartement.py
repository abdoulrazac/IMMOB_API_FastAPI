class Appartement(BaseModel, Base):
    __tablename__ = "appartements"
    adresse = Column(String(30))
    ville = Column(String(30))
    taille = Column(Integer)
    nb_chambre = Column(Integer)
    prix = Column(Integer)
    loyer_min = Column(Integer) 
    disponible = Column(Boolean)
    
    def dict(self):
        return{
            "adresse": self.adresse,
            "ville": self.ville,
            "taille": self.taille,
            "nb_chambre": self.nb_chambre,
            "prix": self.prix,
            "loyer_min": self.loyer_min,
            "disponible": self.disponible
        }