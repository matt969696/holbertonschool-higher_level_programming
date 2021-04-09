#!/usr/bin/python3
""" Simple module """
import requests
import sys


def main():
    """displays the value of the variable X-Request-Id"""
    r = requests.get(sys.argv[1])
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))

if __name__ == "__main__":
    main()
