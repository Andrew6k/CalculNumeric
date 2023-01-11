

def citire_matrice(path):
    readM = open(path,"r")
    n = readM.readline()
    readM.readline()
    memorare = []
    for i in range(int(n)):
        memorare.append([]) #2022 vectori
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
    return memorare

def value(matrice, i ,j):
    if i < j:
        x = i
        i = j
        j = x
    for element in matrice[i]:
        if element[1] == j:
            return element[0]
    return 0

def adunare(matriceA, matriceB):
    adunare = []
    for i in range(len(matriceA)):
        adunare.append([])
    indici = []
    for i in range(0, len(matriceA)):
        for element in matriceA[i]:
            for element2 in matriceB[i]:
                if element[1] == element2[1]:
                    adunare[i].append([element[0]+element2[0],element[1]])
                    indici.append(element[1])
        for element in matriceA[i]:
            if element[1] not in indici:
                adunare[i].append([element[0],element[1]])
        for element in matriceB[i]:
            if element[1] not in indici:
                adunare[i].append([element[0],element[1]])
        indici.clear()
    for i in range(len(matriceA)):
        adunare[i].sort(key=lambda x: x[1])
    return adunare

def inmultireMatrice(matriceA, matriceB):
    inmultire = []
    for i in range(len(matriceA)):
        inmultire.append([])
    for i in range(0,5):
        print(i)
        for j in range(0, len(matriceA)):
            sum = 0
            for k in range(0, len(matriceB)):
                sum = sum + value(matriceA, i ,k) * value(matriceB, k ,j)
            if sum != 0:
                inmultire[i].append([sum,j])
    for element in inmultire:
        if element:
            print(element)

def verificare(adunare,matrice):
    notEqual =[]
    for i in range(0, len(adunare)):
        for element in adunare[i]:
            for element2 in matrice[i]:
                if element[1] == element2[1]:
                    if element[0] != element2[0]:
                        notEqual.append([element[0],element2[0],i,element[1]])
if __name__ == '__main__':
    matriceA = citire_matrice("a.txt")
    matriceB = citire_matrice("b.txt")
    matriceaAB = citire_matrice("a_plus_b.txt")
    matriceaAA = citire_matrice("a_ori_a.txt")
    # for element in matriceA:
    #    print(element)
    inmultire = inmultireMatrice(matriceA, matriceA)

    # adunare = adunare(matriceA,matriceB)
    # for element in adunare:
    #     print(element)
    verificare(inmultire,matriceaAA)