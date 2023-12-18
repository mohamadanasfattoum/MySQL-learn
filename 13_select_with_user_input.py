from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)

mycursor = myconn.cursor()

sql = ' SELECT * FROM products WHERE name=%s '
data = ('samsung 21',)

mycursor.execute(sql ,data)

myresult = mycursor.fetchall()


print (myresult)


print ('selected successfully')
