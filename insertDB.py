import MySQLdb
import csv
import conf2 as cf
from sqlalchemy import create_engine
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date

#needed configuration and connection
meta = MetaData()
conn = MySQLdb.connect(host='34.87.39.39', user='root', password='Dz(_11@HeR#VL', database='corona')
cursor = conn.cursor()
engine = create_engine('mysql://cf.user:cf.password@34.87.39.39:3306/cf.db')

#creating table
corona = Table(
   'corona', meta, 
   Column('date', Date,), 
   Column('country', String(255)), 
   Column('confirmed', Integer()),
   Column('recovered', Integer()),
   Column('deaths', Integer()),
)

meta.create_all(engine)
print("Table Created! %s" %(corona.columns.keys()))

#inserting to the table
csv_data = csv.reader(open('../data/data.csv'))
header = next(csv_data)
print('Inserting in Process ...!')
for row in csv_data:
    print(row)
    cursor.execute(
        "INSERT INTO corona (date,country,confirmed,recovered,deaths) VALUES (%s, %s, %s, %s, %s)", row)

conn.commit()
cursor.close()
print('Process Done!')
print("Table Created! %s" %(corona.columns()))