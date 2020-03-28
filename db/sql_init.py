"""Code to start a mysql db usin pymysql and XAMPP (mysql server with apache)"""

import pymysql

mydb = pymysql.connect(user='root',
                       password='',
                       host='localhost',
                       database='tcsdb')

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE tcsdb")

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), truckmodel VARCHAR(255), "
                 "manufacturer VARCHAR(255), plate VARCHAR(255), date VARCHAR(255), hour VARCHAR(255))")

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#    print(x)

# sql = "INSERT INTO customers (name, truckmodel, manufacturer, plate) VALUES (%s, %s, %s, %s)"
# val = ("John", "X3", "BMW", "MGO1670")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
