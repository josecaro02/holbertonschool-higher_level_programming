#!/usr/bin/python3


def pascal_triangle(n):

    lista = []
    for i in range(n):
        lista.append([])
    for i in range(n):
        if i == 0:
            lista[0].append(1)
            continue
        if i == 1:
            lista[1].append(1)
            lista[1].append(1)
            continue
        for j in range(i + 1):
            if j == 0 or j == i:
                lista[i].append(lista[i-1][j-1])
            else:
                res = lista[i-1][j] + lista[i-1][j-1]
                lista[i].append(res)
    return(lista)
