from databaseSQ import engine, Base
from model import User

Base.metadata.create_all(bind=engine)