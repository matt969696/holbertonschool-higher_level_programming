#!/usr/bin/python3
"""
Module that contains 2 simple classes : BaseGeometry and Rectangle
"""


class BaseGeometry:
    """Simple empty class """

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates that value is a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Simple rectangle class"""

    def __init__(self, width, height):
        """ Init method for Rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
