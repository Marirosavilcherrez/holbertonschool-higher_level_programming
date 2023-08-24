#!/usr/bin/python3
"""This is a Without ORM that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb

"Stablish conexion with the data base"
conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
        db="hbtn_0e_0_usa",
        charset="utf8"
        )
"Create a cursor to execute queries"
cur = conn.cursor()
"Execute a SELECT query and order by the "id" column"
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
"Iterate through the results and display them"
for row in query_rows:
    print(row)
"Close the cursor and the connection"
cur.close()
conn.close()
