#!/usr/bin/python3
"""

Module used to multibly two metrix with numpy

"""

import numpy as ny


def lazy_matrix_mul(m_a, m_b):
    """ multiby two matrix
    parameters: m_a and m_b should be a list of list
    return new metrix contain myltiply"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")
    if any(not isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("Each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("Each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return ny.matmul(m_a, m_b)
