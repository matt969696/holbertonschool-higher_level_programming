#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    mymax = my_list[0]
    for elem in my_list:
        if elem > mymax:
            mymax = elem
    return mymax
