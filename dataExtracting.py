try:
  import os
  import numpy
  import pandas as pd
  import mysql.connector as conn
except Exception as e:
  print(f'Error while implementing!\n {e}')

#creating connection
dbConnection = conn.connect(host='sql6.freesqldatabase.com',
                            user='sql6410935', passwd='GHh4XfMTfT',
                            db='sql6410935', port=3306)
#check if connection established!
print(f'Connection ... \n{dbConnection}')

#lets get some data from the database
data = pd.read_sql_query('SELECT * FROM corona', dbConnection)
print(f'Extracting all Data...\n{data}')