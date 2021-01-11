#!/usr/bin/python3
"""
N Queens main file. For creating a program that solves the nqueens algorithm.
"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except:
    print("N must be a number")
    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)


def updateDic(mysol):
    """ Compute a dictionary of possible positions for non placed queens"""
    mydict = {}
    for k in range(n):
        mydict[k] = list(range(n))
    for k in range(n):
        if mysol[k] != -1:
            mydict[k] = [mysol[k]]
            for i in range(k + 1, n):
                if mysol[k] in mydict[i]:
                    mydict[i].remove(mysol[k])
                if (mysol[k] + i - k) in mydict[i]:
                    mydict[i].remove(mysol[k] + i - k)
                if (mysol[k] - i + k) in mydict[i]:
                    mydict[i].remove(mysol[k] - i + k)
    return mydict


def solvefork(mysol, k, n):
    """
    Recursively solve the Queens problem knowing the placement
    of the first k - 1 queens
    """
    if k == n:
        out = []
        for i in range(n):
            out.append([i, mysol[i]])
        print(out)
        return True

    mydict = updateDic(mysol)
    for i in range(k, n):
        if len(mydict[i]) == 0:
            return False
    while len(mydict[k]) > 0:
        sol = mydict[k].pop(0)
        mysol[k] = sol
        solvefork(mysol, k + 1, n)
    mysol[k] = -1


def main():
    """ Main function to compute possible results """
    mysol = {}
    for k in range(n):
        mysol[k] = -1
    solvefork(mysol, 0, n)

if __name__ == "__main__":
    main()
