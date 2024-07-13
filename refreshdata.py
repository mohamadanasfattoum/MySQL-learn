from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    # database = 'refresh'
)

mycursor = myconn.cursor()

mycursor.execute(" CREATE DATABASE refresh ")



print('All Done!')