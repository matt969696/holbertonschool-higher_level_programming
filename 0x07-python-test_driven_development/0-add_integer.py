#!/usr/bin/python3
"""
0-add_integer module - Contains simple function add_integer
"""


def add_integer(a, b=98):
    """
    Return the sum of a and b
    a and b must be integers or floats
    If a number is a float, it is first cast into an integer
    The result is always an integer
    """
    if a != a or a == float("inf") or a == float("-inf"):
        raise TypeError("a must be an integer")
    if b != b or b == float("inf") or b == float("-inf"):
        raise TypeError("b must be an integer")
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
