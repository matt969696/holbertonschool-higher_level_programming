#!/usr/bin/python3
"""
This module defines a new class : Base
"""


import json
import csv


class Base:
    """ Definition of Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class init """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of a list_dictionaries"""
        if list_dictionaries is None:
            return str([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        myl = []
        if list_objs is not None:
            for elem in list_objs:
                myl.append(cls.to_dictionary(elem))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(myl))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        myl = []
        try:
            with open(filename, 'r') as f:
                myl = cls.from_json_string(f.read())
            for i in range(len(myl)):
                myl[i] = cls.create(**myl[i])
        except:
            pass
        return myl

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save as serialized list of Base objects in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """loads a serialized list of Base objects in csv"""
        filename = cls.__name__ + ".csv"
        myl = []
        try:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    myl.append(obj)
        except:
            pass
        return myl
