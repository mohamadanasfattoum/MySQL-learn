from project.secrets import DATABASE_PASSWORD
import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    passwd = DATABASE_PASSWORD, 
    database = 'pflanzen'
)

mycursor = myconn.cursor()

# mycursor.execute(" CREATE TABLE pflanzen (name VARCHAR(50), farben VARCHAR(100), farben VARCHAR(500)) ")
# mycursor.execute(' DROP TABLE cars')
# ------------
# mycursor.execute(" ALTER TABLE pflanzen ADD id INT AUTO_INCREMENT PRIMARY KEY ") 
# ----------

sql = "INSERT INTO pflanzen (name, farben, description) VALUES(%s ,%s, %s)"
data = [('Kektus','gelb','Lorem ipsum dolor sit amet aliquid a!'),('Tulpen','rot','Lorem ipsum dolor sit amet aliquid a!'),('Rose','rot,rose,blau','Lorem ipsum dolor sit amet aliquid a!')]
mycursor.executemany(sql, data)


myconn.commit()
print('All Done!')
