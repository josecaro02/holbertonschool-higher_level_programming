#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is ".format(number), end='')
if number < 0:
    n_number = (number * -1) % 10
    str0 = "and is less than 6 and not 0"
    print("-{:d} {}".format(n_number, str0) if n_number > 0 else "0 and is 0")
else:
    p_number = number % 10
    if p_number > 6:
        str1 = "and is greater than 6 and not 0"
    elif p_number > 0:
        str1 = "and is less than 6 and not 0"
    print("{:d} {}".format(p_number, str1) if p_number != 0 else "0 and is 0")
