from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config



DB_NAME = config('DB_NAME')
engine_psql = create_engine(DB_NAME)

SessionLocal = sessionmaker(autocommit=False,autoflush=True,bind=engine_psql)

Base = declarative_base()
metadata = MetaData()
metadata.create_all(engine_psql)
def get_psql_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
