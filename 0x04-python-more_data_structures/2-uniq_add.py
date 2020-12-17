#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = list(set(my_list))
    s = 0
    for i in unique:
        s += i
    return s
