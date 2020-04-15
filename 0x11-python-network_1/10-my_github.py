#!/usr/bin/python3
""" Make a request to GitHub API """
from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(response.json().get('id'))
