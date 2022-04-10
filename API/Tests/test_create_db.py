import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

import datetime 
from sqlalchemy.ext.declarative import declared_attr
Base = declarative_base()

class ClasseBase(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)
    create_at  = Column(DateTime, default = datetime.datetime.utcnow())
    update_at  = Column(DateTime, default = datetime.datetime.utcnow())


class User(ClasseBase, Base):
    __tablename__ = "users"
    user_name = Column(String(30))
    password = Column(String(30))
    nom = Column(String(30))
    prenom = Column(String(30))
    tel = Column(Integer)
    user_type = Column(Boolean)
    date_naissance = Column(DateTime)
    trash = Column(Boolean)
    email = Column(String(70))


engine = create_engine('sqlite:///test.db', echo=True)
Base.metadata.create_all(engine)