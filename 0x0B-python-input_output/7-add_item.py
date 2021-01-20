#!/usr/bin/python3
"""
This module contains a simple JSON script
"""
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'
if __name__ == "__main__":
    """ adds all arguments to a Python list, and then save them to a file"""
    if os.path.exists(filename):
        try:
            olist = load_from_json_file(filename)
        except:
            olist = []
    else:
        olist = []
    for arg in range(1, len(sys.argv)):
        olist.append(sys.argv[arg])
    save_to_json_file(olist, filename)
