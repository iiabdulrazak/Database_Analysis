try:
  import os
  import numpy
  import pandas as pd
  import seaborn as sns
  import matplotlib.pyplot as plt
  import mysql.connector as conn
  import matplotlib_inline
except Exception as e:
  print(f'Error while implementing!\n {e}')

#getting environment variables
dbUser = os.getenv('testUserDB')
password = os.environ.get('testPassDB')

#creating connection
dbConnection = conn.connect(host='sql6.freesqldatabase.com',
                            user='sql6410935', passwd='GHh4XfMTfT',
                            db='sql6410935', port=3306)

print(f'Connection ... \n{dbConnection}')