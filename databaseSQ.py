from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

conn_str = 'sqlite:///' + os.path.join(BASE_DIR, 'users.db')


engine = create_engine(conn_str, echo=True)

Base = declarative_base()

Session = sessionmaker()