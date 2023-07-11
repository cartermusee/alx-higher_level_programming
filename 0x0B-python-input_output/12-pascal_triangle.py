#!/usr/bin/python3
'''module for pascal_triangle'''


def pascal_triangle(n):
    """funct for pascal triangle"""
    rows = [[1 for b in range(j + 1)] for j in range(n)]
    for n in range(n):
        for j in range(n - 1):
            rows[n][j + 1] = sum(rows[n - 1][j:j + 2])
    return rows
