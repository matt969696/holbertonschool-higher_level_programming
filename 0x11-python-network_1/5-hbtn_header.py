#!/usr/bin/python3
""" Simple module """
import requests
import sys


def main():
    """displays the value of the variable X-Request-Id"""
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))

if __name__ == "__main__":
    main()
