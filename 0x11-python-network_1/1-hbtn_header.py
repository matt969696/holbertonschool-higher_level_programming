#!/usr/bin/python3
""" Simple module """
from urllib import request
import sys


def main():
    """ displays the value of the X-Request-Id variable """
    with request.urlopen(sys.argv[1]) as response:
        reqid = response.info()["X-Request-Id"]
        print(reqid)

if __name__ == "__main__":
    main()
