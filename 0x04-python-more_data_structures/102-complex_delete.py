#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lkey = list(a_dictionary.keys())
    for key in lkey:
        if a_dictionary[key] == value:
            del(a_dictionary[key])
    return a_dictionary
