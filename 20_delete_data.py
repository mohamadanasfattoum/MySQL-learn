from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)

mycursor = myconn.cursor()

# mycursor.execute(' DELETE FROM products WHERE name = "samsung a 52 s" ')


sql = ' DELETE FROM products WHERE name =%s '
data = ('samsung a 54',)

mycursor.execute(sql , data) # with user input

myconn.commit()

print ('deleted successfully')
