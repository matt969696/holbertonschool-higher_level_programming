#!/usr/bin/python3
"""
Module that contains a simple classe : MyInt
"""


class MyInt(int):
    """Simple class """

    def __eq__(self, other):
        """ Modify the equal method"""
        if int(self) == int(other):
            return False
        return True

    def __ne__(self, other):
        """ Modify the not equal method"""
        if int(self) == int(other):
            return True
        return False
