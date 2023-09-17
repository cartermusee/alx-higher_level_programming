#!/usr/bin/python3
"""
Write a script that lists all
states with a name starting with N
(upper N)
from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    create a connection and list states
    list all states with n
    order by ascending order
    """

    db_connection = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        passwd=argv[2], db=argv[3])
    cur = db_connection.cursor()

    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY 'N%' \
                ORDER BY id ASC")

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db_connection.close()
