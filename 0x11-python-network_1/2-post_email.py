#!/usr/bin/python3
""" Simple module """
from urllib import request, parse
import sys


def main():
    """ request to the passed URL with the email as a parameter """
    values = {}
    values['email'] = sys.argv[2]
    data = parse.urlencode(values)
    data = data.encode('ascii')
    with request.urlopen(sys.argv[1], data) as response:
        resp = response.read().decode('utf-8')
        print(resp)

if __name__ == "__main__":
    main()
