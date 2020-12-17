#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sor = sorted(a_dictionary.keys())
    for elem in sor:
        print("{}: {}".format(elem, a_dictionary[elem]))
