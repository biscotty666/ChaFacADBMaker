from curses import echo
from email.policy import default
from sqlalchemy.orm import declarative_base, sessionmaker, relationships
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey, create_engine

from datetime import datetime
import os

Base = declarative_base()

BASE_DIR = os.path.dirname(os.path.relpath(__file__))
connection_string = "sqlite:///"+os.path.join(BASE_DIR, 'cfa.db')
engine = create_engine(connection_string, echo=True)

Session = sessionmaker()



# 
#
# 
  
