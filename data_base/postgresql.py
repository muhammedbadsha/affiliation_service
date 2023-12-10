from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config



DB_NAME = config('DB_NAME')
engine_psql = create_engine(DB_NAME)

SessionLocal = sessionmaker(autocommit=False,autoflush=True,bind=engine_psql)

Base = declarative_base()

def get_psql_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
