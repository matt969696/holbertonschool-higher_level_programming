#!/usr/bin/python3
"""
This module contains a simple function for Pascal triangle
"""


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascals triangle of n"""
    if n <= 0:
        return []
    outlist = [[1]]
    for i in range(1, n):
        prevlist = outlist[i - 1]
        newlist = [1]
        for k in range(0, i - 1):
            newlist.append(prevlist[k] + prevlist[k + 1])
        newlist.append(1)
        outlist.append(newlist)
    return outlist
