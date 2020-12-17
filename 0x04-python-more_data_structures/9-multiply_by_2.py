#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = {}
    for k, v in a_dictionary.items():
        newdict[k] = v * 2
    return newdict
