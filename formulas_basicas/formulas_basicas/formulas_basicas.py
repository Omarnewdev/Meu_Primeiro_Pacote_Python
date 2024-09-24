import math

def soma(x,y):
    return x+y

def resta(x,y):
    return x-y

def division(x,y):
    return x/y

def multiplicaco(x,y):
    return x*y

def distancia_entre_dois_pontos(x1,y1,x2,y2):
    return math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))

print("{0:.5f}".format(distancia_entre_dois_pontos(2,3,4,5)))
