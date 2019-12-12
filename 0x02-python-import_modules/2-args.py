#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    len_argv = len(sys.argv)
    if len_argv == 1:
        print("0 arguments.")
    elif len_argv == 2:
        print("{:d} argument:".format(len_argv - 1))
    else:
        print("{:d} arguments:".format(len_argv -1))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
