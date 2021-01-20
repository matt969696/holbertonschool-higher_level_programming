#! /usr/bin/env python
""" Try to replace string in heap running process """
import re
import sys


def main():
    """ find and replace string in heap"""
    if len(sys.argv) != 4:
        print("Usage : read-write_heap.py pid search_string replace_string")
        return 1

    pid = sys.argv[1]
    searched = sys.argv[2]
    replacing = sys.argv[3]

    with open("/proc/{:d}/maps".format(int(pid)), "r") as maps:
        for line in maps.readlines():
            if "heap" in line:
                m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
                start = int(m.group(1), 16)
                print("{:02x}".format(start))
                end = int(m.group(2), 16)
                print("{:02x}".format(end))
                break

    with open("/proc/{:d}/mem".format(int(pid)), "rb+") as mem:
        mem.seek(start)
        myread = mem.read(end - start)
        found = myread.find(searched.encode())
        print("{:02x}".format(found))
        mem.seek(start + found)

        mem.write(replacing.encode() + b'\x00')

        mem.seek(start)
        myread = mem.read(end - start)
        found = myread.find(searched.encode())
        print("{:02x}".format(found))

if __name__ == "__main__":
    main()
