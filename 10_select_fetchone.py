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
# mycursor.execute(' SELECT name , description FROM products ') # just name
mycursor.execute(' SELECT name FROM products ') # just name

# myresult = mycursor.fetchall() # to print one from all
# print (myresult[2])

myresult = mycursor.fetchone() # to print one from all
print (myresult)

print ('selected successfully')
