from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'refresh'
)

mycursor = myconn.cursor()

# mycursor.execute(" CREATE DATABASE refresh ") # 1

# 2 -------------------  SHOW DATABASES
# mycursor.execute(" SHOW DATABASES ")


# for db in mycursor:
#     print(db)

# 3 -------------------  
mycursor.execute(" CREATE TABLE cars (name VARCHAR(100) , plot VARCHAR(500)) ")


print ('table created successfully')



print('All Done!')