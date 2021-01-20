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

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        if attributes is in attrs
        """
        islistofstring = True
        if type(attrs) is not list:
            islistofstring = False
        else:
            for elem in attrs:
                if type(elem) is not str:
                    islistofstring = False

        if islistofstring is False:
            return self.__dict__

        return {k: self.__dict__[k] for k in (self.__dict__.keys() & attrs)}

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        if json:
            self.__dict__ = json
