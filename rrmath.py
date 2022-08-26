"""
MATH LIBRARY
"""

from math import sqrt


def matrix_product(A, B):
    result = [[x*0 for x in range(4)] for i in range(4)]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def identity(num):
    m = []
    for row in range(0, num):
        m.append([])
        for col in range(0, num):
            if (row == col):
                m[row].append(1)
            else:
                m[row].append(0)
    return m

def dot(A, B):
    return sum([x*y for x,y in zip(A, B)])


def multiply_vectors(matrix, v):
    return [dot(r, v) for r in matrix]


def subtract(A,B):
     size = isinstance(A, list) + 2 * isinstance(B, list)
     if size == 3:
         return [subtract(ra,rb) for ra,rb in zip(A,B)]
     if size == 2:
         return [subtract(A,rb) for rb in B]
     if size == 1: 
         return [subtract(ra,B) for ra in A]
     return A - B


def cross_product(A, B):
    return [A[1] * B[2] - A[2] * B[1],
            A[2] * B[0] - A[0] * B[2],
            A[0] * B[1] - A[1] * B[0]]
    

def normalize(list):
    return sqrt(((list[0] - list[1]) ** 2)
              + ((list[1] - list[2]) ** 2)
              + ((list[2] - list[0]) ** 2))


def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]


def inverse_matrix(a):
    tmp = [[] for _ in a]

    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret


def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("cant inverse matrix")

        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)

    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)

    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)

    return a
