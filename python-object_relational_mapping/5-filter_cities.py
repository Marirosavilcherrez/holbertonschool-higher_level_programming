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
    state_name = sys.argv[4]
    cur = conn.cursor()
    query = "SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))
    query_rows = cur.fetchall()
    city_names = [row[0]for row in query_rows]
    print(", ".join(city_names))
    cur.close()
    conn.close()
