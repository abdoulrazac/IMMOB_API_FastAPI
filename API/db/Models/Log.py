class Log(BaseModel, Base):
    __tablename__  = "logs"
    tentative_connexion=Column(DateTime)
    id_user = Column(Integer, ForeignKey('users.id'))