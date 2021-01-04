#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except IndexError:
            quotient = 0
            print("out of range")
        except ZeroDivisionError:
            quotient = 0
            print("division by 0")
        except TypeError:
            quotient = 0
            print("wrong type")
        finally:
            res.append(quotient)

    return res
