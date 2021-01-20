#!/usr/bin/python3
"""
This module contains a class : Student
"""


class Student:
    """ Simple class with public instance attributes :
        first_name
        last_name
        age
    """

    def __init__(self, first_name, last_name, age):
        """ initialization method for Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance"""
        return self.__dict__
