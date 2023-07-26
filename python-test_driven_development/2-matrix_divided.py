#!/usr/bin/python3
"""This is a module divided
The module supply one function, 
the division matrix and div.
"""


def matrix_divided(matrix, div):
    """Return the division of a matrix and a div,
    return a float with 2 decimals."""
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    if not all (len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = []
        for i in matrix:
            new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
        return (new_matrix)
