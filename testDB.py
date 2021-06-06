try:
    import csv
    import pandas as pd
    import mysql.connector as conn
except Exception as e:
    print(f'Error while implementing!\n {e}')

#creating connection
dbConnection = conn.connect(host='34.87.39.39',
                            user='root', passwd='Dz(_11@HeR#VL',
                            db='corona', port=3306)
#init the cursor
cursor = dbConnection.cursor()
#check if connection established!
print(f'Connection ... \n{dbConnection}\n')

checkQuery = '''
                SELECT * FROM corona
             '''

outputQuery1 = pd.read_sql_query(checkQuery, dbConnection)
print(outputQuery1)