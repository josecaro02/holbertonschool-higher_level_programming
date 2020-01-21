#!/usr/bin/python3
'''Function that multiplies 2 matrix
Matrix should be of integers or floats
Returns the new matrix

'''

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    ''' This func raise Type errors
    checks if the matrix can be multiplied
    returns new matrix
    '''
    if type(m_a) != list:
        raise ValueError('Lazy: m_a must be a list')
    else:
        for i in m_a:
            if type(i) != list:
                raise ValueError('Lazy: m_a must be a list of lists')

    if type(m_b) != list:
        raise ValueError('Lazy: m_b must be a list')
    else:
        for i in m_b:
            if type(i) != list:
                raise ValueError('Lazy: m_b must be a list of lists')
    if len(m_a) == 0:
        raise TypeError("Lazy: m_a can't be empty")
    if len(m_b) == 0:
        raise TypeError("Lazy: m_b can't be empty")

    for i in m_a:
        if len(i) == 0:
            raise TypeError("Lazy: m_a can't be empty")

    for i in m_b:
        if len(i) == 0:
            raise TypeError("Lazy: m_b can't be empty")

    for i in m_a:
        for i_1 in i:
            if type(i_1) != int and type(i_1) != float:
                msg = 'Lazy: m_a should contain only integers or floats'
                raise ValueError(msg)

    for j in m_b:
        for j_1 in j:
            if type(j_1) != int and type(j_1) != float:
                msg = 'Lazy: m_b should contain only integers or floats'
                raise ValueError(msg)

    size_m_1 = len(m_a[0])
    size_m_2 = len(m_b[0])

    for i in m_a:
        if len(i) != size_m_1:
            raise ValueError('Lazy: each row of m_a must be of the same size')
    for j in m_b:
        if len(j) != size_m_2:
            raise ValueError('Lazy: each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise TypeError("Lazy: m_a and m_b can't be multiplied")

    a = np.array(m_a)
    b = np.array(m_b)
    c = np.matmul(a, b)
    return(c)
