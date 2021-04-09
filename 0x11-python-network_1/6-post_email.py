#!/usr/bin/python3
""" Simple module """
import requests
import sys


def main():
    """displays the value of the variable X-Request-Id"""
    mydic = {}
    mydic['email'] = sys.argv[2]
    r = requests.post(sys.argv[1], data=mydic)
    print(r.text)

if __name__ == "__main__":
    main()
