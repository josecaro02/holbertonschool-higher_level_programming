#!/usr/bin/python3
'''Function that divides a matrix into a num
the maxtrix should be entirely of numbers
Returns the new matrix

'''


def matrix_divided(matrix, div):
    '''This function raise TypeError if the matrix is not a
    list of a lists of integers or floats or if the each row of the
    matrix has not the same size
    '''
    new_mtx = [row[:] for row in matrix]
    if div == 0:
        raise ZeroDivisionError('division by zero')
    else:
        arr_sz = len(matrix[0])
        for i in range(len(matrix)):
            if arr_sz != len(matrix[i]):
                raise TypeError('Each row of the matrix must have the same size')
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) != int and\
                   type(matrix[i][j]) != float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                value = matrix[i][j] / div
                new_mtx[i][j] = round(value, 2)
        return(new_mtx)
