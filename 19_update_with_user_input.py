from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)

mycursor = myconn.cursor()

sql = 'UPDATE products SET description =%s WHERE name =%s'
data = ('update with user input', 'xiaomi 12t')

mycursor.execute(sql , data)


myconn.commit()

print ('updated successfully')
