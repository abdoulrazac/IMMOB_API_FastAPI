import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

import datetime 

Base = declarative_base()

class ClasseBase(Base):
    id = Column(Integer, primary_key=True)
    create_at  = Column(DateTime, default = datetime.datetime.utcnow())
    update_at  = Column(DateTime, default = datetime.datetime.utcnow())


class User(ClasseBase):
    __tablename__ = "users"
    user_name = Column(String(30))
    password = Column(String(30))
    nom = Column(String(30))
    prenom = Column(String(30))
    tel = Column(Int(10))
    user_type = Column(bool)
    date_naissance = Column(Date)
    trash = Column(bool)
    email = Column(String(70))


engine = create_engine('sqlite:///test.db', echo=True)
Base.metadata.create_all(engine)