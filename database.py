''' creates postgres table for mta turnstile data'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Time

Base = declarative_base()


class Readings(Base):
    ''' Creates table for mta ridership '''
    __tablename__ = 'readings'

    id = Column(Integer, primary_key=True)
    ca = Column(String(100))
    unit = Column(String(5))
    scp = Column(String(10))
    station = Column(String(100))
    linename = Column(String(26))
    division = Column(String(10))
    date = Column(Date)
    time = Column(Time)
    desc = Column(String(30))
    entries = Column(Integer)
    exits = Column(Integer)

