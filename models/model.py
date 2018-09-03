from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Testplan(Base):
    __tablename__ = 'testplan'
    idtestplan = Column(Integer, primary_key=True)
    title = Column(String(32))
