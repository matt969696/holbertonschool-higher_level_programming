#!/usr/bin/python3
"""
Add an attribute to an object
"""


def add_attribute(obj, name, attr):
    """ Add an attribute to an object"""
    if "__dict__" in dir(obj):
        setattr(obj, name, attr)
    else:
        raise TypeError("can't add new attribute")
