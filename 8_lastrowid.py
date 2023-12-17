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
data = [
('samsung a 52' , 'Die guten samsung Handys finden sich in der samsung A-Serie'),
('samsung a 54' , 'Die guten samsung Handys finden sich in der samsung A-Serie..'),
('samsung a 52 s' , 'Die guten samsung Handys finden sich in der samsung A-Serie.....')
]

mycursor.executemany(sql , data)
myconn.commit() # to save data in databases

print ('insert was successfully')

print(mycursor.lastrowid) # Retrieve the last number of row affected