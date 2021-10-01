from databaseSQ import Base
from sqlalchemy import Column, Integer, Boolean, Text, String

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    username = Column(String(25), unique=True)
    email = Column(String(100), unique=True)
    password = Column(Text, nullable=True)
    is_active = Column(Boolean, default=False)

    def __repr__(self):
        return f'<User{self.username}>'