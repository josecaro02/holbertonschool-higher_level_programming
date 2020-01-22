#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    counter = 0
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.readlines()

    with open(filename, 'w') as f:
        lista = []
        for line in text:
            lista.append(line)
            if search_string in str(line):
                lista.append(new_string)
        list_str = ''.join(map(str, lista))
        f.write(list_str)
