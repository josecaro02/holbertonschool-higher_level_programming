#!/usr/bin/python3
''' Prints cities in the state and database given'''
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    sql = "SELECT cities.name FROM cities JOIN states \
    ON cities.state_id = states.id  WHERE states.name = %s"
    name_state = (sys.argv[4], )
    cur.execute(sql, name_state)
    result = cur.fetchall()
    for i in range(len(result)):
        print(result[i][0], end="")
        if i != len(result) - 1:
            print(", ", end="")
    print("")
    cur.close()
    db.close()
