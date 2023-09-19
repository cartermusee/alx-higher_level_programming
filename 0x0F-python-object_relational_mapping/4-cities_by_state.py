#!/usr/bin/python3
"""
script that lists all cities
from the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    create a connection and list cities
    order by ascending order
    """

    db_connection = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        passwd=argv[2], db=argv[3])
    cur = db_connection.cursor()

    cur.execute("SELECT * FROM cities \
                ORDER BY id ASC")

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db_connection.close()
