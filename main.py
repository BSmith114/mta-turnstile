'''creates tables and import turnstile data'''
from sqlalchemy import create_engine, Table, MetaData
import database as db
import turnstile
import requests as r
from io import StringIO
import csv

engine = create_engine('postgresql://postgres:specials@localhost/mta')
db.Base.metadata.create_all(engine)
meta = MetaData(bind=engine)
readings = Table('readings', meta, autoload=True)

link = turnstile.mta_turnstile_readings()[0]

html = r.get(link)
text = html.text

data = csv.reader(StringIO(text))

data.__next__()

data_list = list(data)