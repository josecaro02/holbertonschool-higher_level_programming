#!/usr/bin/python3
''' Prints states that matches with 'Arizona' in a database given '''
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cur.execute(sql.format(sys.argv[4]))
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()
