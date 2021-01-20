#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics"""
import sys


if __name__ == "__main__":
    """ Code to retrieve and display datas"""
    size = 0
    statdict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def displaystat(size, statdict):
        """ function to print the stats"""
        print("File size: {}".format(size))
        for key, value in sorted(statdict.items()):
            if value != 0:
                print("{}: {}".format(key, value))

    nbline = 0
    try:
        for line in sys.stdin:
            linetok = line.split(" ")
            if len(linetok) >= 2:
                stat = int(linetok[-2])
                if stat in statdict:
                    statdict[stat] += 1
                    nbline += 1

                try:
                    size += int(linetok[-1])
                except:
                    continue

            if nbline % 10 == 0:
                displaystat(size, statdict)

    except KeyboardInterrupt:
        displaystat(size, statdict)
        raise
    displaystat(size, statdict)
