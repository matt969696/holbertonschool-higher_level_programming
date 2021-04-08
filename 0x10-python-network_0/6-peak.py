#!/usr/bin/python3
""" Module containing find-peak function """


def find_peak(list_of_integers):
    """ Function that find peaks recursively """
    n = len(list_of_integers)
    lis = list_of_integers
    if n == 0:
        return None
    if n == 1:
        return lis[0]
    m = n // 2
    if (m + 1 < n and lis[m] <= lis[m + 1]):
        return find_peak(lis[m + 1:])
    if (lis[m - 1] >= lis[m]):
        return find_peak(lis[:m])
    return lis[m]
