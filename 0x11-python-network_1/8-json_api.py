#!/usr/bin/python3
""" Simple module """
import requests
import sys


def main():
    """displays the value of the variable X-Request-Id"""
    url = "http://0.0.0.0:5000/search_user"""
    mydic = {}
    if len(sys.argv) == 1:
        mydic['q'] = ""
    else:
        mydic['q'] = sys.argv[1]
    r = requests.post(url, data=mydic)
    try:
        json = r.json()
        if not json or len(json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()
