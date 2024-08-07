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
# mycursor.execute('SELECT name FROM cars') # to show just selected column name
# ----------

# myresult = mycursor.fetchall()
# print(myresult[0]) # to print just one with index number
# for _ in myresult:
#     print (_)

# # 2 -------------- 
# myresult = mycursor.fetchone() # with fetchone
# print(myresult)

# 3 ---------------- WHERE
# mycursor.execute('SELECT * FROM cars WHERE id = 1') 
# mycursor.execute('SELECT * FROM cars WHERE name = "BMW"')  
# 4 ---------------- with like
# mycursor.execute('SELECT * FROM cars WHERE name like"%1%"')  
# 5 --------------
# mycursor.execute('SELECT * FROM cars ORDER BY name ')  # ORDER BY name
# mycursor.execute('SELECT * FROM cars ORDER BY name DESC ')  # ORDER BY name DESC

# 6 ---------------------
# mycursor.execute('SELECT * FROM cars LIMIT 5 ') # with limit number
mycursor.execute('SELECT * FROM cars LIMIT 5 OFFSET 3 ') # with limit number with OFFSET 

 



myresult = mycursor.fetchall() 
for _ in myresult:
    print(_)


print('All Done!')
