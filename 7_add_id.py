from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)

mycursor = myconn.cursor()
mycursor.execute(" ALTER TABLE products ADD id INT AUTO_INCREMENT PRIMARY KEY ")
#  I assumed that the id column should be of type INT and have an auto-incrementing feature,
#  which means that each new row inserted into the table will automatically be assigned a unique value for the id column.
#  The PRIMARY KEY constraint indicates that the id column will be the primary key for the table.


print ('add id was successfully')
