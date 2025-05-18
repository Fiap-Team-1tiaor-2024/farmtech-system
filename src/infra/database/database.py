from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config
import os

db_user = config("DB_USER")
db_password = config("DB_PASSWORD")
db_url = config("DB_URL")
db_name = config("DB_NAME")

engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_url}/{db_name}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()