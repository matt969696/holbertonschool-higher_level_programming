#!/usr/bin/python3
"""
101-lazy_matrix_mul module - Contains simple function matrix_mul
"""

from numpy import dot


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices
    Return the new matrix
    The 2 matrix must be multiable
    All elements of the 2 matrix must be integers or floats
    """
    outmat = dot(m_a, m_b)
    return (dot(m_a, m_b))
