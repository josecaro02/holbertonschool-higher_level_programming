#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    for i in range(size - 1, -1, -1):
        print("{:d}".format(my_list[i]))
