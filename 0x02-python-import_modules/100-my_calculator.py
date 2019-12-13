#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argc = len(sys.argv)
    ops = ['+', '-', '*', '/']
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        for i in range(4):
            if ops[i] == sys.argv[2]:
                if i == 0:
                    res = a + b
                elif i == 1:
                    res = a - b
                elif i == 2:
                    res = a * b
                else:
                    res = a // b
                print("{:d} {:s} {:d} = {:d}".format(a, sys.argv[2], b, res))
                break
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
