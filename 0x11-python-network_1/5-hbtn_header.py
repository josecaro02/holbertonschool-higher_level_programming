#!/usr/bin/python3
""" Make a request using request """
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
