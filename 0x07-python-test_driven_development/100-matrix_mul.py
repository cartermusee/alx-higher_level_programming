#!/usr/bin/python3
"""Module with a function that
multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ function multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication

    Raises:
        TypeError: if m_a or m_b is not a list
        TypeError: if m_a or m_b is not a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b are not of the same size
        ValueError: if m_a and m_b cannot be multiplied

    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")

    for j in m_b:
        if not isinstance(j, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for i in m_a:
        for j in i:
            if not type(j) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for i in m_b:
        for j in i:
            if not type(j) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    length = 0

    for i in m_a:
        if length != 0 and length != len(i):
            raise TypeError("each row of m_a must be of the same size")
        length = len(i)

    length = 0

    for j in m_b:
        if length != 0 and length != len(j):
            raise TypeError("each row of m_b must be of the same size")
        length = len(j)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m1 = []
    n1 = 0

    for a in m_a:
        m2 = []
        n2 = 0
        num = 0
        while (n2 < len(m_b[0])):
            num += a[i1] * m_b[i1][n2]
            if n1 == len(m_b) - 1:
                n1 = 0
                n2 += 1
                m2.append(num)
                num = 0
            else:
                n1 += 1
        m1.append(m2)

    return m1
