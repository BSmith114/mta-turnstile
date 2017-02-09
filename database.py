''' creates postgres table for mta turnstile data'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Time

Base = declarative_base()


class Readings(Base):
    ''' Creates table for mta ridership '''
    __tablename__ = 'readings'

    id = Column(Integer, primary_key=True)
    CA = Column(String(100))
    UNIT = Column(String(5))
    SCP = Column(String(10))
    STATION = Column(String(100))
    LINENAME = Column(String(26))
    DIVISION = Column(String(10))
    DATE = Column(Date)
    TIME = Column(Time)
    DESC = Column(String(30))
    ENTRIES = Column(Integer)
    EXITS = Column(Integer)

