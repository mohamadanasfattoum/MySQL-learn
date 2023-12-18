from project.secrets import DATABASE_PASSWORD
import mysql.connector
import random

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'mydb'
)

mycursor = myconn.cursor()

sql = 'UPDATE products SET price = %s WHERE id = %s'

mycursor.execute("SELECT id FROM products")
rows = mycursor.fetchall()

for row in rows:
    product_id = row[0]
    random_price = round(random.uniform(400.99, 1500.99), 2)
    mycursor.execute(sql, (random_price, product_id))

myconn.commit()

print('Updated successfully')
