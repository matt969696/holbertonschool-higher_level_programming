#!/usr/bin/python3
import math
""" MagicClass : Class description"""

class MagicClass:
    """ MagicClass

    Attributes :
    radius(int or float)

    Methods :
    area
    circumference
    """
    def __init__(self, radius):
        """ Init function """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ return area """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ retrun circumference """
        return (2 * math.pi * self.__radius)
