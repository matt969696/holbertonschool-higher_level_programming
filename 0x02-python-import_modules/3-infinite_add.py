#!/usr/bin/python3


def main():
    import sys

    sum = 0

    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i + 1])

    print("{:d}".format(sum))


if __name__ == "__main__":
    main()
