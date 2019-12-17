#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        ta_1 = tuple_a[0]
        ta_2 = tuple_a[1]
    elif len(tuple_a) == 1:
        ta_1 = tuple_a[0]
        ta_2 = 0
    else:
        ta_1 = ta_2 = 0
    if len(tuple_b) >= 2:
        tb_1 = tuple_b[0]
        tb_2 = tuple_b[1]
    elif len(tuple_b) == 1:
        tb_1 = tuple_b[0]
        tb_2 = 0
    else:
        tb_1 = tb_2 = 0
    return((ta_1 + tb_1, ta_2 + tb_2))
