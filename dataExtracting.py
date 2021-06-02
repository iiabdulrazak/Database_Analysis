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
corona_show = pd.read_sql_query('SHOW TABLES FROM sql6410935', dbConnection)
corona_describe = pd.read_sql_query('DESCRIBE corona', dbConnection)
corona_select = pd.read_sql_query('SELECT * FROM corona', dbConnection)

print(f'Show all Tables:\n{corona_show} \n\n Describe Table:\n{corona_describe} \n\n Select all Data:\n{corona_select}')