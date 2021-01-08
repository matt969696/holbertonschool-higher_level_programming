#!/usr/bin/python3
"""
2-matrix_mul module - Contains simple function matrix_mul
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices
    Return the new matrix
    The 2 matrix must be non null list of list
    The 2 matrix must be multiable
    All elements of the 2 matrix must be integers or floats
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for line in m_a:
        if type(line) is not list:
            raise TypeError("m_a must be a list of lists")

    for line in m_b:
        if type(line) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for line in m_a:
        for a in line:
            if type(a) is not int and type(a) is not float:
                raise TypeError("m_a should contain only integers or floats")

    for line in m_b:
        for a in line:
            if type(a) is not int and type(a) is not float:
                raise TypeError("m_b should contain only integers or floats")

    for line in m_a:
        if len(line) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for line in m_b:
        if len(line) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    linea = len(m_a)
    cola = len(m_a[0])
    lineb = len(m_b)
    colb = len(m_b[0])

    if cola != lineb:
        raise ValueError("m_a and m_b can't be multiplied")

    outmat = []
    for i in range(linea):
        totline = []
        for j in range(colb):
            tot = 0
            for k in range(cola):
                tot += m_a[i][k] * m_b[k][j]
            totline.append(tot)
        outmat.append(totline)

    return(outmat)
