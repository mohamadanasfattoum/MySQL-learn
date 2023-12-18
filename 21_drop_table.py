from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)

mycursor = myconn.cursor()


# mycursor.execute('DROP TABLE brand') # delete the table
mycursor.execute('DROP TABLE IF EXISTS brand') 


myconn.commit()

print ('deleted successfully')
