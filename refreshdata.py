from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    # database = 'refresh'
)

mycursor = myconn.cursor()

# mycursor.execute(" CREATE DATABASE refresh ") # 1

# 2  SHOW DATABASES
mycursor.execute(" SHOW DATABASES ")


for db in mycursor:
    print(db)




print('All Done!')