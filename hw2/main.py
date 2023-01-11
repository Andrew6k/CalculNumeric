import sys
import json
import math
import numpy as np
import numpy.linalg


def validare(A):
    #matrice pozitiva
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] < 0:
                return False
    #matrice simetrica
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                return False
    return True

def pivot(l, A):
    n=len(A)
    max = -1
    for i in range(n):
        if A[i][l] > max:
            max = A[i][l]
            pos = i
    print(pos)
    if pos > l:
        for i in range(n + 1):
            x = A[l][i]
            A[l][i] = A[pos][i]
            A[pos][i] = x

def pivot_inversa(l, A):
    n = len(A1)
    max = -1
    for i in range(n):
        if A1[i][l] > max:
            max = A1[i][l]
            pos = i
    print(pos)
    if pos > l:
        for i in range(n):
            x = A1[l][i]
            A1[l][i] = A1[pos][i]
            A1[pos][i] = x

            x = I3[l][i]
            I3[l][i] = I3[pos][i]
            I3[pos][i] = x

def calcul(i):
    val = 0
    for j in range(i+1,n):
        val = val + A[i][j]*x_var[j]
    return val

if __name__ == '__main__':
    file_handler = open("input", 'r')
    data = json.load(file_handler)
    A = np.array(data[0])
    global A1
    A1 = A
    b = np.array(data[1])
    n = np.array(data[2])
    b = np.reshape(b, (n,1))
    b1 = b
    print(A)

    print(validare(A))

    print(b)
    #print(n)
    global epsilon
    epsilon = 10**(-6)
    l=0
    A = np.append(A, b, axis=1)
    pivot(l, A)
    while l<=n-2 and abs(A[l][l])>epsilon:
        for i in range(l + 1, n):
            A[i][l] = A[i][l] / A[l][l]
            for j in range(l + 1, n + 1):
                A[i][j] = A[i][j] - A[i][l] * A[l][j]
                #print("look",A[i][j])
        l = l + 1
        pivot(l, A)
    print(A)
    ok = 0
    for i in range(n):
        if A[l][l] <= epsilon and ok == 0:
            print("singular matrix")
            ok = 1
    if ok == 0:
        global x_var
        x_var = np.zeros((3,1))
        for i in range(n-1,0,-1):
            print(A[i][i])
            if(A[i][i]>0):
                x_var[i] = (b[i] - calcul(i))/A[i][i]

        print(x_var)

    #verificare
    for i in range(n):
        for j in range(n):
            A[i][j] = A[i][j]*x_var[i]
    for i in range(n):
        A[i][0] = A[i][0] - b[i]

    print(numpy.linalg.norm(A))

    x_new=numpy.linalg.solve(A1,b1)
    print(x_new)
    A_inv = numpy.linalg.inv(A1)
    print(A_inv)
    A_putere = numpy.linalg.matrix_power(A1,-1)
    print(A_putere)
    #print(A)

    global I3
    I3 = numpy.matrix('1 0 0; 0 1 0; 0 0 1')
    l = 0
    pivot_inversa(l, A1)
    while l <= n - 1 :
        for i in range(l + 1, n):
            x = A1[i][l] / A1[l][l]
            for j in range(l + 1, n):
                A1[i][j] = A1[i][j] - x * A1[l][j]
        for i in range(l + 1, n):
            for j in range(l + 1, n):
                I3[i][j] = I3[i][j] - x * I3[l][j]
        for i in range(l + 1, n):
            A1[i][l] = 0
        l = l + 1
        pivot_inversa(l, A1)
