import os

#creating env-variable for database, for more secure way to connect
#set environment variables
os.environ['testUserDB'] = "sql6410935"
os.environ['testPassDB'] = "GHh4XfMTfT"

print(f'DB_USER: {os.environ["testUserDB"]}, DB_PASS: {os.environ["testPassDB"]}')
