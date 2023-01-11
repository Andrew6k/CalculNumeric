import numpy as np

def citire_matrice(path):
    readM = open(path,"r")
    n = readM.readline()
    readM.readline()
    memorare = []
    for i in range(int(n)):
        memorare.append([])
    for readLine in readM:
        if readLine != '\n':
            line = readLine.split(',')
            val = float(line[0])
            linie = int(line[1])
            coloana = int(line[2])
            ok = False
            if coloana <= linie:
                for element in memorare[linie]:
                    if element[1] == coloana:
                        element[0] = element[0] + val
                        ok = True
                if ok == False:
                    memorare[linie].append([val,coloana]) #append (valoare,coloana)
    for i in range(int(n)):
        memorare[i].sort(key=lambda x: x[1])
    return n, memorare


def value(matrice, i ,j):
    if i < j:
        x = i
        i = j
        j = x
    for element in matrice[i]:
        if element[1] == j:
            return element[0]
    return 0

def citire_vector(path):
    readV = open(path,"r")
    memorare = []
    for readline in readV:
        val = float(readline)
        memorare.append(val)
    return memorare


def diagonala (matrice, n):
    diag = []
    for i in range(int(n)):
        for j in matrice[i]:
            if j[1] == i:
                diag.append(j[0])
    return  diag

def verif_diag(diag, n, epsilon):
    for i in range(int(n)):
        if abs(diag[i]) < epsilon:
            return False
    return True

if __name__ == '__main__':
    n, matriceA = citire_matrice("a_5.txt")
    vectorB = citire_vector("b_6.txt")
    epsilon = 10**(-6)
    # for element in matriceA:
    #     print(element)
    #print(vectorB)
    #print(n)
    diag = diagonala(matriceA, n)
    print(diag)
    print(verif_diag(diag, n, epsilon))

    x_c = list(0 for c in range(int(n)))
    x_p = list(0 for c in range(int(n)))
    k = 0
    k_max = 1000
    delta_max = pow(10,8)

    for i in range (int(n)):
        x_c[i] = vectorB[i]/diag[i]
    delta_x = np.linalg.norm(np.subtract(x_c, x_p))
    print("Norma 0", delta_x)
    k = k+1
    while epsilon<= delta_x <= delta_max and k <= k_max:
        x_p = x_c.copy()
        s1 = list(0 for x in range(int(n)))
        for i in range(1, int(n)):
            sum = 0
            for j in range(i):
                #ok = 0
                for elem in matriceA[i]:
                    if j == elem[1] :
                        #ok = 1
                        sum += elem[0] * x_p[j]
                        break
            s1[i] = sum

        s2 = list(0 for x in range(int(n)))
        for j in range(int(n) - 1):
            sum = 0
            for i in range(j+1, int(n)):
                for elem in matriceA[i]:
                    if j == elem[1] :
                        sum += elem[0] * x_p[i]
                        break
            s2[j] = sum

        for i in range(int(n)):
            x_c[i] = (vectorB[i] - s1[i] - s2[i]) / diag[i]
        delta_x = np.linalg.norm(np.subtract(x_c,x_p))
        print(f'Norma {k}',delta_x)
        k = k + 1
    if delta_x < epsilon:
        a_xc = list(0 for i in range(int(n)))
        for i in range(int(n)):
            row = list(0 for x in range(int(n)))
            if 0 < i:
                for k in range(i):
                    for elem in matriceA[i]:
                        if k == elem[1]:
                            row[k] = elem[0]
            for k in range(i, int(n)):
                for elem in matriceA[i]:
                    if i == elem[1]:
                        row[k] = value(matriceA, k, i)
            for j in range(int(n)):
                a_xc[i] += row[j] * x_c[j]
        print("x_c:",x_c)
        print("Infinite norm", np.linalg.norm(np.subtract(a_xc,vectorB),np.inf))

    else:
        print("Divergent")