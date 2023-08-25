#!/usr/bin/python3
"""Without ORM that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


if __name__ == "__main__":
    "List all states from the database with 4 arguments"
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    state_name = sys.argv[4]  # state name searched
    cur = conn.cursor()
    query = "SELECT id, name FROM states WHERE name=%s\
                    ORDER BY id ASC"
    cur.execute(query, (state_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
