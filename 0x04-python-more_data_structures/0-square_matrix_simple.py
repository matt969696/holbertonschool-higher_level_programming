#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for vec in matrix:
        vecs = list(map(lambda x: x*x, vec))
        res.append(vecs)
    return res
