#!/usr/bin/env python3
import MySQLdb
import sys

if __name == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    sql = "SELECT * FROM states"
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()
