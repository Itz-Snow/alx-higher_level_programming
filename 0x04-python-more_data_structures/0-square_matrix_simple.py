#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # create an empty result matrix of the same size as the input matrix
    result = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    # iterate over each element of the input matrix and compute its square
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][j] ** 2
    # return the resulting matrix
    return result
