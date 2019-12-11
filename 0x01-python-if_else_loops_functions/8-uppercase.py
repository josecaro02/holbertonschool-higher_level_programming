#!/usr/bin/python3
def uppercase(str):
    for i in str + "\n":
        if ord(i) > 96 and ord(i) < 123:
            print("{:s}".format(chr(ord(i)-32)), end="")
        else:
            print("{:s}".format(i), end="")
