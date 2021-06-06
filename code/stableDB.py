try:
    import csv
    import pandas as pd
    import mysql.connector as conn
except Exception as e:
    print(f'Error while implementing!\n {e}')

#creating connection and configuration

config ={
    'user': 'root',
    'password': 'Dz(_11@HeR#VL',
    'host': '34.87.39.39',
    'database': 'corona'
}
dbConnection = conn.connect(**config)
#init the cursor
cursor = dbConnection.cursor()
#check if connection established!
print(f'Connection ... \n{dbConnection}')

#Inserting to the table
csv_data = csv.reader(open('../data/data2.csv'))
header = next(csv_data)
print('Inserting in Process ...!')
for row in csv_data:
    print(row)
    cursor.execute(
        "INSERT INTO corona (date,country,confirmed,recovered,deaths) VALUES (%s,%s,%s,%s,%s)", row)

#Outputing the results
dbConnection.commit()
cursor.close()
dbConnection.close()
print('Process Done!')