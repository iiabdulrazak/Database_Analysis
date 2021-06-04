try:
    import re
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

createQuery = '''
                CREATE TABLE IF NOT EXISTS corona(date DATE, country VARCHAR(255),
                confirmed INT(50), recovered INT(50), deaths INT(50))
              '''

checkQuery = '''
                SELECT * FROM coron
             '''
             
insertQuery = '''
                INSERT INTO corona(id,date,country,confirmed,recovered,deaths) VALUES(%s,%s,%s,%s,%s,%s)
             '''
             
#creating variable out of csv file
data = pd.read_csv('data/data.csv')
ids = data.index
date = data['date']
country = data['country']
confirmed = data['confirmed']
recovered = data['recovered']
deaths = data['deaths']

allVariables = (date,country,confirmed,recovered,deaths)
cursor.execute(insertQuery, allVariables)
dbConnection.commit()

#lets print the output from the database
print(checkQuery, dbConnection)
