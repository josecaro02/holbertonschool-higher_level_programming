#!/usr/bin/python3
""" Makes a POST request to a given URL """
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as response:
        print(response.code)
