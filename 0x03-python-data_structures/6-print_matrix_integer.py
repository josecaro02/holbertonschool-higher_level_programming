#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if len(matrix) != 1:
        for i in range (len(matrix)):
            for j in range (len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end = '')
                if j < len(matrix[i]) - 1:
                    print(" ", end = '')
                if j == (len (matrix[i]) - 1):
                   print("")

    else:
        print("")
