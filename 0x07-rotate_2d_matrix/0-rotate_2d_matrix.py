#!/usr/bin/env python3
"""Rotation of 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix
    
    Arg:
        matrix (int): 2D arrays to rotate.
    
    Return:
        The rotated matrix in-place.
    """
    matrix_len = len(matrix)
    
    # Transpose the matrix first
    for i in range(matrix_len):
        for j in range(i + 1, matrix_len):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each roll
    for i in range(matrix_len):
        matrix[i].reverse()
