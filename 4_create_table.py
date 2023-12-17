from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)


mycursor = myconn.cursor()
mycursor.execute(" CREATE TABLE products (name VARCHAR(100) , plot VARCHAR(500)) ")


print ('table created successfully')