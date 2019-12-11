#!/usr/bin/python3
num = 1
for i in range(122, 96, -1):
    if(num % 2 == 0):
        j = i - 32
    else:
        j = i
    print("{:s}".format(chr(j)), end="")
    num +=1
