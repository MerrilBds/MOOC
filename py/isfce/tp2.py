import math
def calculdistanceradiant(vitesse:int,angle:float)->float:
    assert 1 <= angle <=89,'angle compris entre 1 et 89 inclus'
    d = (2*vitesse**2*math.cos(angle)*math.sin(angle))/9.8
    return d
print(calculdistanceradiant(10,30))


