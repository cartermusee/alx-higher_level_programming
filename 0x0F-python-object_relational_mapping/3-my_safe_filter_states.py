#!/usr/bin/python3
"""
script that takes in
an argument and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    create a connection and list states
    list all states as per users input
    prevent sql injection
    order by ascending order
    """

    db_connection = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        passwd=argv[2], db=argv[3])
    cur = db_connection.cursor()

    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY %s \
                ORDER BY id ASC", (argv[4],))

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db_connection.close()
