#!/usr/bin/python3
""" Make a request using urllib """
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print(r)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: OK")
