from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import create_engine
from .utils import settings


data_base_uri=settings.dburi
engine=create_engine(data_base_uri)


localsession =sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db=localsession()
    try:
        yield db
    finally :
        db.close()