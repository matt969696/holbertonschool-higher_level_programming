#!/usr/bin/python3
""" Simple module """
import requests
import sys


def main():
    """uses the GitHub API to display your id"""
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                              sys.argv[1])
    json = requests.get(url).json()
    for i in range(len(json)):
        myj = json[i]
        print("{}: {}".format(myj.get("sha"),
                              myj.get("commit").get("author").get("name")))
        if i == 9:
            break

if __name__ == "__main__":
    main()
