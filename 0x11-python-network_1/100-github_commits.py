#!/usr/bin/python3
""" Make a request to GitHub API """
import requests
import sys


if __name__ == "__main__":
    try:
        url = "https://api.github.com/repos/{}/{}/commits".\
              format(sys.argv[2], sys.argv[1])
        response = requests.get(url)
        for i in range(-10, 0):
            print("{}: ".format(response.json()[i].get('sha')), end="")
            print("{}".format(response.json()[i].get('commit').get('author')
                              .get('name')))
    except ValueError:
        print("Not a valid JSON")
