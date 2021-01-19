#!/usr/bin/python3
"""
Module that contains a simple class : BaseGeometry
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
