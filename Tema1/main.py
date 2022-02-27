import math
#ex1
import random


def print_nr():
    m=-1
    while(True):
        u=10**m #precizia masina
        if 1.0+u==1.0:
            break
        m=m-1
    return m+1

#ex2
def non_associative():
    #a
    a=1.0
    u=10**print_nr()
    b=u/10
    c=u/10
    print((a+b)+c)
    print(a+(b+c))
    print((a+b)+c==a+(b+c))
    print()

    #b
    a=0.4 # 0.multiplu de 2
    u=10**print_nr()
    b=u/10
    c=u/10
    print((a*b)*c)
    print(a*(b*c))
    print((a*b)*c==a*(b*c))

#ex3
def sinus(x):
    if abs(x)<=1:
        a=[1805490264.690988571178600370234394843221,
              -164384678.227499837726129612587952660511,
              3664210.647581261810227924465160827365,
              -28904.140246461781357223741935980097,
              76.568981088717405810132543523682]
        b=[2298821602.638922662086487520330827251172,
               27037050.118894436776624866648235591988,
               155791.388546947693206469423979505671,
               540.567501261284024767779280700089,
               1.0]
        y=x**2
        P4=a[0]+y*(a[1]+y*(a[2]+y*(a[3]+y*a[4])))
        Q4=b[0]+y*(b[1]+y*(b[2]+y*(b[3]+y*b[4])))

        if abs(Q4)<10**(-12):
            Q4=10**(-12)

        value=x*P4/Q4
        #print(1/4*math.pi*x)
        print(value)
        print(math.sin(1/4*x*math.pi))
        print(abs(value-math.sin(1/4*x*math.pi)))
    else:
        print("input out of range")

def cosinus(x):
    if abs(x)<=1:
        a=[1090157078.174871420428849017262549038606,
              -321324810.993150712401352959397648541681,
              12787876.849523878944051885325593878177,
              -150026.206045948110568310887166405972,
              538.333564203182661664319151379451]
        b=[1090157078.174871420428867295670039506886,
               14907035.776643879767410969509628406502,
               101855.811943661368302608146695082218,
               429.772865107391823245671264489311,
               1.0]
        y=x**2
        P4=a[0]+y*(a[1]+y*(a[2]+y*(a[3]+y*a[4])))
        Q4=b[0]+y*(b[1]+y*(b[2]+y*(b[3]+y*b[4])))

        if abs(Q4)<10**(-12):
            Q4=10**(-12)

        value=P4/Q4
        #print(1/4*math.pi*x)
        print(value)
        print(math.cos(1/4*x*math.pi))
        print(abs(value-math.cos(1/4*x*math.pi)))
    else:
        print("input out of range")

def logaritm(x):
    if x<=math.sqrt(2) and x>=1/math.sqrt(2):
        a=[75.151856149910794642732375452928,
              -134.730399688659339844586721162914,
              74.201101420634257326499008275515,
              -12.777143401490740103758406454323,
              0.332579601824389206151063529971]
        b=[37.575928074955397321366156007781,
               -79.890509202648135695909995521310,
               56.215534829542094277143417404711,
               -14.516971195056682948719125661717,
               1.0]
        z=(x-1)/(x+1)
        y=z**2
        P4=a[0]+y*(a[1]+y*(a[2]+y*(a[3]+y*a[4])))
        Q4=b[0]+y*(b[1]+y*(b[2]+y*(b[3]+y*b[4])))

        if abs(Q4)<10**(-12):
            Q4=10**(-12)

        value=z*P4/Q4
        #print(1/4*math.pi*x)
        print(value)
        print(math.log(x,10))
        print(abs(value-math.log(x,10)))
    else:
        print("input out of range")

if __name__ == '__main__':
    print(print_nr())
    print(10**print_nr())
    print(1.0+10**(-16))
    print()

    non_associative()
    print()

    sinus(1)
    print()
    cosinus(1)
    print()
    logaritm(0.85)