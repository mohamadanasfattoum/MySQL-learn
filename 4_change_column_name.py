from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)


mycursor = myconn.cursor()
mycursor.execute(" ALTER TABLE products CHANGE COLUMN plot description VARCHAR(500)")


print ('change name was successfully')