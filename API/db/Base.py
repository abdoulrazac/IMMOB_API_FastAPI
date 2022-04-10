from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

import datetime 

Base = declarative_base()

class ClasseBase(Base):
    id = Column(Integer, primary_key=True)
    create_at  = Column(DateTime, default = datetime.datetime.utcnow())
    update_at  = Column(DateTime, default = datetime.datetime.utcnow())