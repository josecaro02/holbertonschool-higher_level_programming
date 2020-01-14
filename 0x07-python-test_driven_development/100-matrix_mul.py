#!/usr/bin/python3
'''Function that multiplies 2 matrix
Matrix should be of integers or floats
Returns the new matrix

'''


def matrix_mul(m_a, m_b):
    if type(m_a) != list:
        raise TypeError('m_a must be a list')
    else:
        for i in m_a:
            if type(i) != list:
                raise TypeError('m_a must be a list of lists')

    if type(m_b) != list:
        raise TypeError('m_b must be a list')
    else:
        for i in m_b:
            if type(i) != list:
                raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for i in m_a:
        if len(i) == 0:
            raise ValueError("m_a can't be empty")

    for i in m_b:
        if len(i) == 0:
            raise ValueError("m_b can't be empty")

    for i in m_a:
        for i_1 in i:
            if type(i_1) != int and type(i_1) != float:
                raise TypeError('m_a should contain only integers or floats')

    for j in m_b:
        for j_1 in j:
            if type(j_1) != int and type(j_1) != float:
                raise TypeError('m_b should contain only integers or floats')

    size_m_1 = len(m_a[0])
    size_m_2 = len(m_b[0])

    for i in m_a:
        if len(i) != size_m_1:
            raise TypeError('each row of m_a must be of the same size')
    for j in m_b:
        if len(j) != size_m_2:
            raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    rows = len(m_a)
    columns = len(m_b[0])
    new_matrix = []
    for i in range(rows):
        new_matrix.append([0] * columns)
    for i in range(len(m_a)):
        for j  in range(len(m_b[0])):
            for x in range(len(m_b)):
                new_matrix[i][j] = new_matrix[i][j] + (m_a[i][x] * m_b[x][j])
    return(new_matrix)
