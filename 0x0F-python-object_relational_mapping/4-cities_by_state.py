#!/usr/bin/python3
"""
module to handle database using python and MYSQLDB
"""
import MySQLdb as MDB
import sys


def showcities(name, pas, database):
    """show the cities"""

    connect = MDB.connect(
        host="localhost", user=name, passwd=pas, db=database, port=3306
    )
    cursor = connect.cursor()
    cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC"""
    )
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

    showcities(name, pas, database)
