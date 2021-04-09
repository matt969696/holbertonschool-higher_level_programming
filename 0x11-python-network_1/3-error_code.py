#!/usr/bin/python3
""" Simple module """
from urllib import request
from urllib import error
import sys


def main():
    """ request to the passed URL with the email as a parameter """
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            resp = response.read().decode('utf-8')
            print(resp)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))

if __name__ == "__main__":
    main()
