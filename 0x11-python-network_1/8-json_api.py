#!/usr/bin/python3
""" Make a request using urllib """
import requests
import sys

if __name__ == "__main__":
    try:
        payload = {'q': sys.argv[1]}
        r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
        res = r.json()
        if len(res) == 0:
            print("No result")
        else:
            print("[{}] {}".format(res['id'], res['name']))
    except ValueError:
        print("Not a valid JSON")
    except IndexError:
        print("No result")
