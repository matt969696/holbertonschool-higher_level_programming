#!/usr/bin/python3
"""
This module contains a simple JSON function
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation"""
    with open(filename, mode='w', encoding='utf-8') as myfile:
        myfile.write(json.dumps(my_obj))
