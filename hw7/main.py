import random

def interval(a):
    A = max(a)
    R = (abs(a[0])+A) / abs(a[0])
    return R

def horner(a, v):
    res = a[0]
    for i in range(1, len(a)):
        res = res*v + a[i]
    return res

if __name__ == '__main__':
    a = [1, -6, 13, -12, 4]
    n = len(a) - 1
    eps = 10**(-6)
    sol = []


    R = interval(a)
    print(R)

    while len(sol)<n:
        k = 0
        kmax = 1000
        x = random.uniform(-R, R)
        x0 = x
        numitor = (horner(a, x+horner(a,x)) - horner(a,x-horner(a,x)))
        y = x - ((2 * (horner(a, x)**2)) / numitor)
        deltaX = (2 * horner(a,x) * ((horner(a,x) + horner(a,y)))) / numitor

        while eps <= abs(deltaX) <= 10**8 and k<=kmax:
            if abs(horner(a,x)) <= eps/10:
                deltaX = 0
            else:
                numitor = (horner(a, x + horner(a, x)) - horner(a, x - horner(a, x)))
                y = x - ((2 * (horner(a, x) ** 2)) / numitor)
                deltaX = (2 * horner(a, x) * ((horner(a, x) + horner(a, y)))) / numitor
                x = x - deltaX
                k += 1

        if abs(deltaX) < eps:
            ok = 0
            for i in sol:
                if abs(x-i) < eps:
                    ok = 1
                    break
            if ok == 0:
                if -R <= x <= R:
                    sol.append(x)
        else:
            print("divergenta")

    print(sol)
    f = open("out.txt", "w")
    for i in sol:
        f.write(str(i))
        f.write(" ")
    f.close()