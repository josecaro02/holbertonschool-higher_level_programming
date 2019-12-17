#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for i in my_list:
            if max < i:
                max = i
        return(max)
    else:
        return (None)
