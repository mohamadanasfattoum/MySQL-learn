from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)

mycursor = myconn.cursor()


mycursor.execute('ALTER TABLE products ADD COLUMN price VARCHAR(20)')
# mycursor.execute('')


print ('add column was successfully')

