#!/usr/bin/python3
"""
3-print_square module - Contains simple function print_square
"""


def print_square(size):
    """
    prints a square with the character #
    size is the size length of the square
    size must be a positive integer
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    for i in range(size):
        print("#" * size)
