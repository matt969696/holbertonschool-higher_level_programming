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
        self.size = size

    @property
    def size(self):
        """
        Getter for size attribute of square object
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter for size attribute of square object
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

    def __eq__(self, other):
        """ Method for eq """
        return (self.area() == other.area())

    def __ne__(self, other):
        """ Method for eq """
        return (self.area() != other.area())

    def __gt__(self, other):
        """ Method for eq """
        return (self.area() > other.area())

    def __lt__(self, other):
        """ Method for eq """
        return (self.area() < other.area())

    def __ge__(self, other):
        """ Method for eq """
        return (self.area() >= other.area())

    def __le__(self, other):
        """ Method for eq """
        return (self.area() <= other.area())
