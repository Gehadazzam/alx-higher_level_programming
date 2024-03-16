#!/usr/bin/python3
"""
module to handle database using python and MYSQLDB
"""
import MySQLdb as MDB
import sys


def showstate(name, pas, database, arg):
    """show the state that match argument"""

    connect = MDB.connect(
        host="localhost", user=name, passwd=pas, db=database, port=3306
    )
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY %(n)s ORDER BY id ASC",
        {"n": arg},
    )
    tab = cursor.fetchall()
    for row in tab:
        print(row)
    cursor.close()
    connect.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    name = sys.argv[1]
    pas = sys.argv[2]
    database = sys.argv[3]
    arg = sys.argv[4]

    showstate(name, pas, database, arg)
