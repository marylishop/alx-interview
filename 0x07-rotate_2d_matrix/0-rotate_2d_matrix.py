#!/usr/bin/python3

"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """ rotate 2D Matrix 90 degrees clockwise
    """
    ln = len(matrix)

    # Swap Rows to Columns
    for i in range(ln):
        for j in range(i, ln):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for lst in matrix:
        lst.reverse()
