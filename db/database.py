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
        sql_new = "INSERT INTO customers (name, truckmodel, manufacturer, plate) VALUES (%s, %s, %s, %s)"

        # use user entered values
        value = (str(name), str(truckmodel), str(manufacturer), str(plate))
        self.cursor.execute(sql_new, value)

        self.mydb.commit()

        print(self.cursor.rowcount, "record inserted.")

    def read_values(self):
        self.cursor.execute("SELECT * FROM customers")
        values_list = self.cursor.fetchall()


        return values_list

    def delete_value(self, index):
        text_del = "DELETE FROM customers WHERE id = "
        id_del = " '12' "
        sql_del = text_del + id_del

        print(sql_del)

        self.connect()
        self.cursor.execute(sql_del)

        self.mydb.commit()
