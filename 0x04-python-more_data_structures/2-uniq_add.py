#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq = set(my_list)
    res = 0
    for i in uniq:
        res = res + i
    return (res)
