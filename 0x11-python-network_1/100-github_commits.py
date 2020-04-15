#!/usr/bin/python3
""" Make a request to GitHub API """
import requests
import sys


if __name__ == "__main__":
    try:
        url = "https://api.github.com/repos/{}/{}/commits".\
              format(sys.argv[2], sys.argv[1])
        response = requests.get(url)
        response = response.json()
        for i in response[:10]:
            print("{}: ".format(i.get('sha')), end="")
            name = i.get('commit').get('author').get('name')
            print("{}".format(name))
    except ValueError:
        print("Not a valid JSON")
