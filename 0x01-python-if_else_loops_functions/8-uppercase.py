#!/usr/bin/python3
def uppercase(str):
    str2 = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            str2 = str2 + chr(ord(c) - 32)
        else:
            str2 = str2 + c
    print("{}".format(str2))
