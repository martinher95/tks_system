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

    def new_value(self, name, truckmodel, manufacturer, plate):
        sql = "INSERT INTO customers (name, truckmodel, manufacturer, plate) VALUES (%s, %s, %s, %s)"

        # use user entered values
        value = (str(name), str(truckmodel), str(manufacturer), str(plate))
        self.cursor.execute(sql, value)

        self.mydb.commit()

        print(self.cursor.rowcount, "record inserted.")

    def read_values(self):
        self.cursor.execute("SELECT * FROM tksdb")
        values_list = self.cursor.fetchall()

        for x in values_list:
            print(x)





