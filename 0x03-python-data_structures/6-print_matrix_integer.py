#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            b_spc = 0
            for j in i:
                if b_spc != 0:
                    print(" ", end='')
                b_spc = 1
                print("{:d}".format(j), end='')
            print("")
