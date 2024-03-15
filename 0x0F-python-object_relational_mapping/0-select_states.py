#!/usr/bin/python3
import MySQLdb
import sys


def show_states(name, pas, database):
    connect = MySQLdb.connect(
        host="localhost", user=name, passwd=pas, db=database, port=3306
    )
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    tab = cursor.fetchall()
    for row in tab:
        print(row)
    cursor.close()
    connect.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    name = sys.argv[1]
    pas = sys.argv[2]
    database = sys.argv[3]

    show_states(name, pas, database)
