from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv('DB_URL')

engine = create_engine(DB_URL)
Base = declarative_base()
session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    session = session_local()
    try:
        yield session
    finally:
        session.close()
