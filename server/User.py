from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(77))
    login = Column(String(77))
    password = Column(String(77))

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    def __repr__(self):
        return "<user(%s, %s, %s)>" % (self.name, self.login, self.password)
