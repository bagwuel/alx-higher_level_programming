#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        new_array = []
        for y in x:
            new_array.append(y * y)
        new_matrix.append(new_array)
    return (new_matrix)
