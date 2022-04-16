class Log(BaseModel, Base):
    __tablename__  = "logs"
    tentative_connexion=Column(DateTime)
    id_user = Column(Integer, ForeignKey('users.id'))

    # Ne pas entrer un attribut pour les clefs étrangères.
    def dict(self):
        return {
            "tentative_connexion": self.tentative_connexion
        }