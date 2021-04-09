#!/usr/bin/python3
""" Simple module """
import requests
import sys


def main():
    """uses the GitHub API to display your id"""
    url = 'https://api.github.com/repos/{0}/{1}/commits'.format(sys.argv[1],
                                                                sys.argv[2])
    json = requests.get(url).json()
    for i in range(10):
        myj = json[i]
        print("{}: {}".format(myj['sha'], myj['commit']['author']['name']))

if __name__ == "__main__":
    main()
