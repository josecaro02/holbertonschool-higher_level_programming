#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        nb = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            nb += 1
        print("")
        return(nb)
    except:
        print("")
        return(nb)
