#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary.items())
    for i in key_list:
        if value == i[1]:
            del a_dictionary[i[0]]
    return (a_dictionary)
