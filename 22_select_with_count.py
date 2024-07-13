from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)

mycursor = myconn.cursor()


mycursor.execute('SELECT * FROM products') 

myresult = mycursor.fetchone()
print (myresult)

print ('counted successfully')
