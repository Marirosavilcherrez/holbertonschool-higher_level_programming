#!/usr/bin/python3
"""Without ORM that lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb


if __name__ == "__main__":
    "List all cities from the database with 3 arguments"
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]  # database name
        )
    cur = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
