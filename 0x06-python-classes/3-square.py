#!/usr/bin/python3
"""
Square Module - Contains simple class definition of Square
"""


class Square:
    """
    Square Class : simple implementation
    """
    def __init__(self, size=0):
        """
        Square Init : initialize a square

        Attributes:
        size (int): Size of the square, must be positive or 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Method that return the current square area
        """
        return (self.__size * self.__size)
