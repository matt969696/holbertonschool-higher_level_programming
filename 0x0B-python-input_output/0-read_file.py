#!/usr/bin/python3
"""
This module contains a simple read function
"""


def read_file(filename=""):
    """  reads a text file (UTF8) and prints it to stdout"""
    with open(filename, mode='r', encoding='utf-8') as myfile:
        print(myfile.read(), end="")
