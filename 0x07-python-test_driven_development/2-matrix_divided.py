#!/usr/bin/python3
"""
2-matrix_divided module - Contains simple function matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    Return the new matrix
    All elements ofd the matrix must be integers or floats
    div must be integer or float, non 0
    The results are rounded to 2 decimal places
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    for line in matrix:
        if type(line) is not list:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")

    for line in matrix:
        for a in line:
            if type(a) is not int and type(a) is not float:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")

    for line in matrix:
        if len(line) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    newmat = [[round(a/div, 2) for a in line] for line in matrix]
    return newmat
