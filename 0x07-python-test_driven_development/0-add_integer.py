#!/usr/bin/python3
'''Function that add 2 numbers( float and integer)
the result will be an integer.
Function return the value.

'''


def add_integer(a, b=98):
    ''' This func raise Type error if any of the numbers
    it's not a integer or a float, otherwise return the add
    '''
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    elif type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    else:
        return (int(a) + int(b))
