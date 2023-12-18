from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)

mycursor = myconn.cursor()

# mycursor.execute(' SELECT * FROM products ORDER BY name ') # تلقائي ترتيب تصاعدي
# mycursor.execute(' SELECT * FROM products ORDER BY id ') # by default aescent
# mycursor.execute(' SELECT * FROM products ORDER BY description ')
mycursor.execute(' SELECT * FROM products ORDER BY id DESC ') # descent ترتيب تنازلي 

myresult = mycursor.fetchall()


for product in myresult:
    print(product)

# print (myresult)


print ('selected successfully')
