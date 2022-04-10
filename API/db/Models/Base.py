from sqlalchemy.ext.declarative import declared_attr
import datetime

class BaseModel(object):
    @declared_attr
    def __tablename__ (cls):
        return cls.__name__.lower()
        
    id = Column(Integer, primary_key=True)
    create_at  = Column(DateTime, default = datetime.datetime.utcnow())
    update_at  = Column(DateTime, default = datetime.datetime.utcnow())


    