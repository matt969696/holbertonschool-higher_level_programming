#!/usr/bin/python3
def print_last_digit(number):
    ld = number % 10
    if ld != 0 and number < 0:
        ld = 10 - ld
    print(ld, end="")
    return (ld)
