from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)

mycursor = myconn.cursor()

sql = 'INSERT INTO products(name , description) VALUES(%s ,%s)'
data = ('xiaomi 13 t' , 'Die besten Xiaomi Handys finden sich in der Xiaomi 13-Serie')

mycursor.execute(sql , data)
myconn.commit() # to save data in databases

print ('insert was successfully')

print(mycursor.rowcount) # Retrieve the number of rows affected