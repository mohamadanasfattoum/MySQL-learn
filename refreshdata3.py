from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'refresh'
)

mycursor = myconn.cursor()
# mycursor.execute('ALTER TABLE cars ADD COLUMN color VARCHAR(30) ') # add neu COLUMN
mycursor.execute('ALTER TABLE cars CHANGE color color VARCHAR(50) ') # CHANGE VARCHAR


myconn.commit()
print('All Done!')
