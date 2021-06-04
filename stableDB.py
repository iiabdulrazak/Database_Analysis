try:
  import pandas as pd
  import mysql.connector as conn
except Exception as e:
  print(f'Error while implementing!\n {e}')

#creating connection
dbConnection = conn.connect(host='34.87.39.39',
                            user='root', passwd='Dz(_11@HeR#VL',
                            db='corona', port=3306)
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
                LOAD DATA INFILE '/home/liquidx/Desktop/sarcasmDet_Database_Analysis/data/data.csv' 
                INTO TABLE corona
                FIELDS TERMINATED BY ',' 
                ENCLOSED BY '"'
                LINES TERMINATED BY '\n'
                IGNORE 1 ROWS;
              '''

#lets get some data from the database
data = pd.read_sql_query(insertQuery, dbConnection)
print(f'Table created...\n{data}')