from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)

mycursor = myconn.cursor()


# mycursor.execute(' SELECT * FROM products  LIMIT 5 ')
mycursor.execute(' SELECT * FROM products  LIMIT 5 OFFSET 2 ') # descent ترتيب تنازلي 

myresult = mycursor.fetchall()


for product in myresult:
    print(product)

# print (myresult)


print ('selected successfully')
