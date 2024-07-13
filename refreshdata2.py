from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'refresh'
)

mycursor = myconn.cursor()
mycursor.execute('SELECT * FROM cars') # to show all selected data 

myresult = mycursor.fetchall()

for _ in myresult:
    print (_)



print('All Done!')
