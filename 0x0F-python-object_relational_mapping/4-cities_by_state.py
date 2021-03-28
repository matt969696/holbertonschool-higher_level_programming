#!/usr/bin/python3
"""
This module contains a simple function
"""


def main():
    """script that lists all cities from the database"""
    import sys
    import MySQLdb

    myh = "localhost"
    myu = sys.argv[1]
    myp = sys.argv[2]
    myd = sys.argv[3]

    db = MySQLdb.connect(host=myh, port=3306, user=myu,
                         passwd=myp, db=myd)
    cur = db.cursor()
    cur.execute("""SELECT a.id, a.name, b.name FROM cities a
    LEFT JOIN states b on a.state_id = b.id
    ORDER BY a.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
