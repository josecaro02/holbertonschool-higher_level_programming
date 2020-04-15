#!/usr/bin/python3
""" Makes a POST request to a given URL """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req, data=data) as response:
        html = response.read().decode('utf-8')
        print(html)
