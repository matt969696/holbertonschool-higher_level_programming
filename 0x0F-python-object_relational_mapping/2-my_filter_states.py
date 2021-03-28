#!/usr/bin/python3
"""
This module contains a simple function to list all states
"""


def main():
    """script that lists all states from the database hbtn_0e_0_usa"""
    import sys
    import MySQLdb

    myh = "localhost"
    myu = sys.argv[1]
    myp = sys.argv[2]
    myd = sys.argv[3]
    mys = sys.argv[4]

    db = MySQLdb.connect(host=myh, port=3306, user=myu,
                         passwd=myp, db=myd)
    cur = db.cursor()
    myquery = "SELECT * FROM states\
    WHERE name LIKE BINARY '{}'\
    ORDER BY id".format(mys)
    cur.execute(myquery)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
