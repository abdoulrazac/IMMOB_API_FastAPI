class User(BaseModel, Base):
    __tablename__ = "users"
    username = Column(String(30))
    password = Column(String(30))
    nom = Column(String(30))
    prenom = Column(String(30))
    tel = Column(Integer)
    usertype = Column(Integer)
    date_naissance = Column(DateTime)
    trash = Column(Boolean, default = False)
    email = Column(String(70))
    salt = Column(String(70))