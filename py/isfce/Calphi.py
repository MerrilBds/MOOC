import math


def calcphi(prec:float)->(int,float):
    ''''Calcule le n'ombre d'itérations pour avoir le nombre Phi avec une précision "prec"'''
    assert 0< prec <=1, "doit être entre 0 < prec <=1"
    f0 = 1
    f1 = 1
    n = 2
    phi = (1 + math.sqrt(5))/2
    while math.fabs(phi-f1 / f0)>prec:
        f2 = f1 + f0
        f0 = f1
        f1 = f2
        n = n + 1
    return n , f1/f0

print(f" le nombre Phi prec O.OO1 est {calcphi(0.001)}")
print(f" le nombre Phi prec O.3 est {calcphi(0.3)}")

