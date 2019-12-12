#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    suma = 0
    for i in range(1, argc):
        suma = suma + int(sys.argv[i])
    print("{:d}".format(suma))
