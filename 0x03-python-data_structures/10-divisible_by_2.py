#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ret = []
    for elem in my_list:
        if elem % 2 == 0:
            ret.append(True)
        else:
            ret.append(False)
    return ret
