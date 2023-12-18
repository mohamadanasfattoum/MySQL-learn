from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)

mycursor = myconn.cursor()


# mycursor.execute(' SELECT * FROM products ')
mycursor.execute(' SELECT name FROM products ') # just name

myresult = mycursor.fetchall() 

for product in myresult:
    print(product)

print ('selected successfully')