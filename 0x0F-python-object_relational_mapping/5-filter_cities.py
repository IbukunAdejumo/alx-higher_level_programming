#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


def get_dbase():
    """Takes arguments argv and list from database
    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    dbase = MySQLdb.connect(host="localhost",
                            port=3306,
                            user=argv[1],
                            passwd=argv[2],
                            db=argv[3],
                            charset="utf8"
                            )
    # Declaring state name
    sname = argv[4]

    # Getting a cursor
    dbase_cur = dbase.cursor()

    # Executing dbase queries
    dbase_cur.execute("SELECT c.name FROM cities AS c\
            INNER JOIN states AS s\
            ON c.state_id = s.id\
            WHERE s.name=%s\
            ORDER BY c.id", (sname,))

    # Fetches all the rows of a query result
    query_rows = dbase_cur.fetchall()

    result = []
    # Print result one in one
    for rows in query_rows:
        result.append(rows[0])

    # Print state names
    print(', '.join(result))

    dbase_cur.close()
    dbase.close()


if __name__ == '__main__':
    get_dbase()
