import random
import numpy as np
m1=[]
m2=[]
m3=[]
#asigna valores de matrices
for i in range(4):
    aux1=[]
    aux2=[]
    aux3=[]
    for j in range(4):
        aux1.append(random.randint(0,10))
        aux2.append(random.randint(0,10))
        aux3.append(random.randint(0,10))
    m1.append(aux1)
    m2.append(aux2)
    m3.append(aux3)
a3=np.matmul(m1,m1)
a3=np.matmul(a3,m1)#matrzi y elevado a 3
b1=np.invert(m2)#matriz 2 invesa
aa3=np.invert(a3)#matr1 y elevado a 3 y luego invertida

ab=np.matmul(a3,b1)#multiplicacion de A a la 3 por b inversa
ab=np.matmul(ab,m3)#multiplica lo de arriba con la matriz c(3)
ms=[]
for i in range(4):
    aux=[]
    for j in range(4):
        aux.append(ab[i][j]+aa3[i][j])
    ms.append(aux)

print("matriz 1")
for a in m1:
    print(a)
print("matriz 2")
for a in m2:
    print(a)
print("matriz 3")
for a in m3:
    print(a)
print("matriz 1 elevado a 3")
for a in a3:
    print(a)
print("matriz b inversa")
for a in b1:
    print(a)
print("matriz 1 elevado a 3 e inversa")
for a in aa3:
    print(a)
