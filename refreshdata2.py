from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'refresh'
)

mycursor = myconn.cursor()
# mycursor.execute('SELECT * FROM cars') # to show all selected data 
# ----------
mycursor.execute('SELECT name FROM cars') # to show just selected column name
# ----------

# myresult = mycursor.fetchall()
# print(myresult[0]) # to print just one with index number
# for _ in myresult:
#     print (_)

# 2 -------------- 
myresult = mycursor.fetchone() # with fetchone
print(myresult)

print('All Done!')
