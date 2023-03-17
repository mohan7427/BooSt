from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a sqlite engine instance
DATABASE_URL = "mysql+pymysql://root:Orange123@172.17.0.2/boost"

engine = create_engine(DATABASE_URL, connect_args= dict(host='172.17.0.2', port=3306))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a DeclarativeMeta instance
Base = declarative_base()
