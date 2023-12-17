from .secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'dbsql'
)


mycursor = myconn.cursor()


cursorobject.execute('CREATE DATABASE')


print('All Done!')