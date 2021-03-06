import pandas as pd
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from datetime import datetime, timedelta

USERNAME = 'postgres'
PASSWORD = 'pass123'
DBNAME = 'postgres'
HOSTNAME = 'localhost'
TABLENAME = 'inputBot_unfollowlog'
DB_STRING = 'postgresql+psycopg2://{}:{}@{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, DBNAME)


@contextmanager
def db_session(db_url):
    engine = create_engine(db_url, convert_unicode=True)
    connection = engine.connect()
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))
    yield db_session
    db_session.close()
    connection.close()


class UnfollowLogManager(object):

    def __init__(self, insta_data_id):
        self.insta_data_id = insta_data_id

    def correctUnfollowLog(self, userArray):

    def getDataFromUnfollowLog(self, days=2, amountUserToUnfollow=0):
        try:
        except Exception as e:
            print(e)
        return data_all

if __name__ == "__main__":
    fl = UnfollowLogManager('niclasguenther')
    fl.correctUnfollowLog(['insta1', 'insta2', 'insta4'])
    users_list = fl.getDataFromUnfollowLog(days=2, amountUserToUnfollow=20)
