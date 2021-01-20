#!/usr/bin/python3
"""
This module contains a simple function to append a text file
"""


def append_after(filename="", search_string="", new_string=""):
    """  inserts a line of text to a file,
    after each line containing a specific string"""
    with open(filename, 'r+') as myfile:
        contents = myfile.readlines()
        i = 0
        while i < len(contents):
            if search_string in contents[i]:
                contents.insert(i + 1, new_string)
                i += 1
            i += 1
        myfile.seek(0)
        myfile.writelines(contents)
