from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mysql'
)


mycursor = myconn.cursor()


cursorobject.execute('CREATE DATABASE')


print('All Done!')