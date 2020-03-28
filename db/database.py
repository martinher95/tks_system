"""Code for database actions and manipulation"""

import pymysql


def connect(db='tcsdb'):
    mydb = pymysql.connect(user='root',
                   password='',
                   host='localhost',
                   database=db)

    return mydb


def new_value(name, truckmodel, manufacturer, plate, date, hour, db='tcsdb'):
    db = connect(db)
    cursor = db.cursor()

    sql_new = "INSERT INTO customers (name, truckmodel, manufacturer, plate, date, hour) " \
              "VALUES (%s, %s, %s, %s, %s, %s)"

    print(date)

    # use user entered values
    value = (str(name), str(truckmodel), str(manufacturer), str(plate), str(date), str(hour))
    cursor.execute(sql_new, value)

    db.commit()

    print(cursor.rowcount, "record inserted.")


def read_values(db='tcsdb'):
    db = connect(db)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM customers")
    values_list = cursor.fetchall()

    return values_list


def delete_value(db='tcsdb'):
    db = connect(db)
    cursor = db.cursor()

    sql_del = "DELETE FROM customers WHERE id = %s"

    try:
        # execute the query
        cursor.execute(sql_del, 13)

        # accept the change
        db.commit()

    except Exception as error:
        print(error)

    finally:
        cursor.close()
        db.close()
        db.commit()
