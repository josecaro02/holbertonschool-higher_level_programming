#!/usr/bin/python3


def number_of_lines(filename=""):

    line_count = 0
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            line_count += 1
    return(line_count)
