from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

import settings

class Basedb():

    def __init__(self):

        Base = declarative_base()
        engine = self.__db_connect()
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def __db_connect(self):
        """
        Performs database connection using database settings from settings.py.
        Returns sqlalchemy engine instance
        """
        return create_engine(URL(**settings.DATABASE))

    def insert_row(self, object):
        """
        Abstraction of create object
        """
        self.session.add(object)
        self.session.commit()
        self.session.close()

    def select_all_rows(self, object):
        """
        Abstraction of list objects
        """
        return self.session.query(object).all()

    