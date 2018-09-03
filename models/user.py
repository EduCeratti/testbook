from sqlalchemy import create_engine, Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = 'user'
    name = Column(String(32)
    email = Column(String(32)
