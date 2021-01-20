#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics"""
import sys


if __name__ == "__main__":
    """ Code to retrieve and display datas"""
    size = 0
    statusdict = {}
    try:
        nbline = 0
        for line in sys.stdin:
            linetok = line.split(" ")
            if len(linetok) != 9:
                continue
            nbline += 1
            size += int(linetok[8])
            stat = linetok[7]
            if stat in statusdict:
                statusdict[stat] += 1
            else:
                statusdict[stat] = 1

            if nbline % 10 == 0:
                print("File size: {}".format(size))
                for key, value in sorted(statusdict.items()):
                    print("{}: {}".format(key, value))

    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for key, value in sorted(statusdict.items()):
            print("{}: {}".format(key, value))
            raise
    if nbline % 10 != 0:
        print("File size: {}".format(size))
        for key, value in sorted(statusdict.items()):
            print("{}: {}".format(key, value))
