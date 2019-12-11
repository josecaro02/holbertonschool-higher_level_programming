#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
p_number = -((number * -1) % 10) if number < 0 else number % 10
if p_number == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, p_number))
elif p_number < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, p_number))
else:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, p_number))
