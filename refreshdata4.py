from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'refresh'
)

mycursor = myconn.cursor()
sql = 'UPDATE cars SET plot = %s WHERE name = %s '
data = ('aasfgilhkjhnbvc','BMW2')
mycursor.execute(sql, data)


myconn.commit()
print('All Done!')
