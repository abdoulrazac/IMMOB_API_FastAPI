from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()


class School(Base):
    __tablename__ = "woot"

    id = Column(Integer, primary_key=True)
    name = Column(String)  

    def __init__(self, name):
                

Base.metadata.create_all(engine)


# POUR SAUVER LES CHANGEMENTS :
# git add *
# git commit --m "message"
# git push