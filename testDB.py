import pandas as pd
import mysql.connector as conn

#creating connection
dbConnection = conn.connect(host='sql6.freesqldatabase.com',
                            user='sql6410935', passwd='GHh4XfMTfT',
                            db='sql6410935', port=3306)

#check if connection established!
print(f'Connection ... \n{dbConnection}\n')

#sql querys to test
query = "SELECT * FROM corona"

#testing sql scripts
data = pd.read_sql_query(query, dbConnection)

#printing excution
print(data)