#!/usr/bin/python3
"""
Module that contains 1 simple classes : Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Simple square class"""

    def __init__(self, size):
        """ Init method for Square class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
