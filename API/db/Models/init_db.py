from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base
import os
import pathlib
# Importer SETTING DATABASE

Base = declarative_base()

path = str(pathlib.Path(__file__).parent.absolute())
exclude_files = ["__init__.py", "Base.py", "init_db.py"]
files = os.listdir(path)

exec(open(path + "/Base.py").read())
for file in files:
    if file not in exclude_files:
        exec(open(path + "/" + file).read())


engine = create_engine('sqlite:///test.db', echo=True)
Base.metadata.create_all(engine)
