"""Code for database actions and manipulation"""

import pymysql


class mysql_connection:
    """mysql connection attempt"""
    def connect(self):
        self.mydb = pymysql.connect(user='root',
                       password='',
                       host='localhost',
                       database = 'tksdb')
        self.cursor = self.mydb.cursor()

    def new_value(self):
        sql = "INSERT INTO customers (name, truckmodel, manufacturer, plate) VALUES (%s, %s, %s, %s)"

        # use user entered values
        value = ("John", "X3", "BMW", "MGO1670")
        self.cursor.execute(sql, value)

        self.mydb.commit()

        print(self.cursor.rowcount, "record inserted.")




