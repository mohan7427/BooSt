from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a sqlite engine instance
DATABASE_URL = "mysql+pymysql://rajat:Orange123@localhost/boost"

engine = create_engine(DATABASE_URL, connect_args= dict(host='localhost', port=3309))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a DeclarativeMeta instance
Base = declarative_base()
