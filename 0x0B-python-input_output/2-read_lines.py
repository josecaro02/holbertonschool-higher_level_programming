#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):

    line_count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
        f.seek(0)
        if nb_lines <= 0 or nb_lines >= line_count:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
