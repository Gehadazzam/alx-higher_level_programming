#!/usr/bin/python3
"""
module to handle database using python and MYSQLDB
"""
import MySQLdb as MDB
import sys


def showcities(name, pas, database, arg):
    """show the cities"""

    connect = MDB.connect(
        host="localhost", user=name, passwd=pas, db=database, port=3306
    )
    cursor = connect.cursor()
    cursor.execute(
        """ SELECT cities.name
        FROM cities JOIN states ON cities.state_id = states.id
        WHERE states.name = %(n)s
        ORDER BY cities.id ASC""",
        {"n": arg},
    )
    tab = cursor.fetchall()
    names = [row[0] for row in tab]
    print(", ".join(names))
    cursor.close()
    connect.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    name = sys.argv[1]
    pas = sys.argv[2]
    database = sys.argv[3]
    arg = sys.argv[4]
    showcities(name, pas, database, arg)
