#!/usr/bin/python3
"""
5-text_identation module - Contains simple function text_identation
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    text must be a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    endsent = 0
    strmod = ""
    for letter in text:
        if letter == '.' or letter == '?' or letter == ':':
            strmod = strmod + letter + '\n' + '\n'
            endsent = 1
        elif letter == ' ':
            if endsent == 0:
                strmod = strmod + letter
        else:
            strmod = strmod + letter
            endsent = 0

    print(strmod, end="")
