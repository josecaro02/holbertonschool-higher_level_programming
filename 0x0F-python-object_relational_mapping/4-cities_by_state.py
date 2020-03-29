#!/usr/bin/python3
''' Prints table with cities and states in a database given '''
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name FROM cities JOIN states \
    ON cities.state_id = states.id ORDER BY cities.id ASC"
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()
