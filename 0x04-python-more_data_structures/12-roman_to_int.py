#!/usr/bin/python3


def roman_to_int(roman_string):
    dict_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    real_str = []
    res = 0

    if type(roman_string) == str and roman_string:
        for i in range(len(roman_string)):
            for j in dict_num.keys():
                if j == roman_string[i]:
                    real_str.append(dict_num[j])
        len_num = len(real_str)
        if len_num == 1:
            return(real_str[0])
        else:
            for i in range(len_num):
                if i + 1 <= len_num - 1 and real_str[i] < real_str[i + 1]:
                    real_str[i] = -1 * real_str[i]
            for i in real_str:
                res = res + i
            return (res)
    else:
        return (0)
