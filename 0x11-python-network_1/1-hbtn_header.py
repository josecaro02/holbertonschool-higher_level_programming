#!/usr/bin/python3
""" Print X-Request-Id of a url request """
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html['X-Request-Id'])
