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

conn = engine.connect()

columns = ['ca', 'unit', 'scp', 'station', 'linename', 'division', 'date', 'time', 'desc', 'entries', 'exits']

links = turnstile.mta_turnstile_readings()[0:5]

for link in links:
    print("Import from: ", link)
    html = r.get(link)
    data = csv.reader(StringIO(html.text))
    data.__next__() #skips headers in first row
    data = [dict(zip(columns, row)) for row in list(data)]
    conn.execute(readings.insert(), data)