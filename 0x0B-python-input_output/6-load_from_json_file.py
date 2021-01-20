#!/usr/bin/python3
"""
This module contains a simple JSON function
"""
import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file"""
    with open(filename, mode='r', encoding='utf-8') as myfile:
        return json.loads(myfile.read())
