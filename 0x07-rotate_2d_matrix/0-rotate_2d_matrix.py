#!/usr/bin/python3
"""2D matrix rotation
"""

def rotate_2d_matrix(matrix):
    if not matrix or not matrix[0]:
        return

    n = len(matrix)

    # Transpose the matrix in-place
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row in the transposed matrix
    for i in range(n):
        matrix[i].reverse()

