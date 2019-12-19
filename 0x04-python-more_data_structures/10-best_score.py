#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        key_list = list(a_dictionary.keys())
        max = a_dictionary[key_list[0]]
        key_max = key_list[0]
        for i in list(a_dictionary.keys()):
            if a_dictionary[i] > max:
                max = a_dictionary[i]
                key_max = i
        return (key_max)
