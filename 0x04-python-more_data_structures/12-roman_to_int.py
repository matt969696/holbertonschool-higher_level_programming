#!/usr/bin/python3
def roman_to_int(roman_string):
    dic1 = dict(M=1000, D=500, C=100, L=50, X=10, V=5, I=1)
    dic2 = dict(CM=900, CD=400, XC=90, XL=40, IX=9, IV=4)

    if isinstance(roman_string, str):
        if roman_string == "":
            return 0
        if roman_string[:2] in dic2.keys():
            return dic2[roman_string[:2]] + roman_to_int(roman_string[2:])
        return dic1[roman_string[:1]] + roman_to_int(roman_string[1:])
