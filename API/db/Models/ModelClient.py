class Client(BaseModel, Base):
    __tablename__ = "clients"
    nom = Column(String(30))
    prenom = Column(String(30))
    date_naissance = Column(DateTime)
    profession = Column(String(30))
    CNI = Column(Integer)
    email = Column(String(70)) 
    tel = Column(Integer)

    def dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance,
            "profession": self.profession,
            "CNI": self.CNI,
            "email": self.email,
            "tel": self.tel
        }
