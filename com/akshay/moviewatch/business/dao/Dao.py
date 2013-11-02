from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

__author__ = 'akshay'

engine = create_engine('mysql://root:sa@localhost:3306/movieWatchUnicode', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()