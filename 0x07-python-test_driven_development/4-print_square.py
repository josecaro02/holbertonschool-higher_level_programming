#!/usr/bin/python3
''' Function that prints squares of # characters
size is the lenght of the square
Doesn't return anything, only prints

'''


def print_square(size):
    '''This function raise Type error if the size if not a
    integer.
    Raise error if size is less than 0.
    '''
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif size == 0:
        return
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
