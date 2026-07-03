#!/usr/bin/python3
"""Rotate a square 2D matrix 90 degrees clockwise in place."""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix: A square matrix represented as a list of lists.
    """
    size = len(matrix)

    for layer in range(size // 2):
        last = size - layer - 1
        for index in range(layer, last):
            offset = index - layer
            top = matrix[layer][index]

            matrix[layer][index] = matrix[last - offset][layer]
            matrix[last - offset][layer] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[index][last]
            matrix[index][last] = top