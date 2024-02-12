#!/usr/bin/python3
"""
Create a function def pascal_triangle(n) that returns a list of lists of
 integers representing the Pascal’s triangle of n:
  * Returns an empty list if n <= 0
  * You can assume n will be always an integer
"""


def pascal_triangle(n):
    """ Create Pascal’s triangle """
    pascalT = []
    if (n > 0):
        for i in range(n):
            row = [1] * (i + 1)

            if i >= 2:
                for j in range(1, i):
                    row[j] = pascalT[i - 1][j - 1] + pascalT[i - 1][j]

            pascalT.append(row)

    return pascalT
