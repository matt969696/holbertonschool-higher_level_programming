#!/usr/bin/python3
""" Simple module """
import requests
import sys


def main():
    """uses the GitHub API to display your id"""
    url = "https://api.github.com/user"
    user = sys.argv[1]
    token = sys.argv[2]
    r = requests.get(url, auth=(user, token))
    json = r.json()
    print(json.get('id'))

if __name__ == "__main__":
    main()
