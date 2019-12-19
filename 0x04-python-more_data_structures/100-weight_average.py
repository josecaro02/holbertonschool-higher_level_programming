#!/usr/bin/python3


def weight_average(my_list=[]):
    scores = 0
    weight = 0
    if my_list:
        for i in my_list:
            scores = scores + (i[0] * i[1])
            weight = weight + i[1]
        return (scores/weight)
    else:
        return (0)
