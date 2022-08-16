"""
MATH LIBRARY
"""

from math import sqrt
from numpy import matrix, subtract, linalg

def dot_product(a: list, b: list):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

def negative(i: int):
    return -i

def matrix_product(x: list, y: list):
    return [[sum(a*b for a,b in zip(x_row,y_col)) for y_col in zip(*y)] for x_row in x]

def cross_product(a: list, b: list):
    m = [a,
         b]

    return [m[0][1] * m[1][2] - m[1][1] * m[0][2], 
          -(m[0][0] * m[1][2] - m[0][2] * m[1][0]),
            m[0][0] * m[1][1] - m[0][1] * m[1][0]]

def normalize(v: list):
    u = 0
    res = []
    for i in v:
        u += i**2
    u = sqrt(u)
    for i in v:
        res.append(i/u)
    return res

def substract(a, b):
    return subtract(a,b)

def weird_matrix(a: list):
    return matrix(a)

def inverse_matrix(a):
    return linalg.inv(a)
