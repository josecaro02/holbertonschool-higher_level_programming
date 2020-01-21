#!/usr/bin/python3
''' Function that prints
My name is <first name> <last name>
If only first name is given, the program
don's show error
'''


def say_my_name(first_name, last_name=""):
    if type(first_name) != str or\
       type(last_name) != str:
        raise TypeError('first_name must be a string or last_name must be a string')
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
