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
data = [('samsung 21' , 'Die besten samsung Handys finden sich in der samsung s-Serie'),
('samsung 22' , 'Die besten samsung Handys finden sich in der samsung s-Serie..'),
('samsung 23' , 'Die besten samsung Handys finden sich in der samsung s-Serie.....')
]

mycursor.executemany(sql , data)
myconn.commit() # to save data in databases

print ('insert was successfully')

print(mycursor.rowcount) # Retrieve the number of rows affected