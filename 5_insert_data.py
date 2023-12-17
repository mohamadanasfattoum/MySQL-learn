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
data = ('xiaomi 12t' , 'Spitzenkameras, erstklassige Displays und hohe Geschwindigkeit: Xiaomi Handys punkten in jeder Hinsicht.')

mycursor.execute(sql , data)
myconn.commit() # to save data in database

print ('insert was successfully')