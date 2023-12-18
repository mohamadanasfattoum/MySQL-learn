from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)

mycursor = myconn.cursor()


# mycursor.execute('UPDATE products SET price = "400" WHERE name = "xiaomi 12t" ')

mycursor.execute('UPDATE products SET price = "400" ')


myconn.commit()

print ('updated successfully')

