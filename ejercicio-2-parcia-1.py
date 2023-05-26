import random
import numpy as np

matriz1=[]
matriz2=[]
matriz3=[]
ms=[]
#asigna valores de matrices
for i in range(3):
    aux1=[]
    aux2=[]
    aux3=[]
    for j in range(3):
        aux1.append(random.randint(1,10))
        aux2.append(random.randint(11,30))
        aux3.append(random.randint(-10,-1))
    matriz1.append(aux1)
    matriz2.append(aux2)
    matriz3.append(aux3)
#suma matriz 1 y 2
for i in range(3):
    aux=[]
    for j in range(3):
        aux.append(matriz1[i][j]+matriz2[i][j])
    ms.append(aux)

#multiplica la matriz suma y la 3

mr=(np.matmul(ms,matriz3))

ma=(np.matmul(matriz1,matriz3))
mb=(np.matmul(matriz2,matriz3))
#suma matriz a*c y B*c
mrr=[]
for i in range(3):
    aux=[]
    for j in range(3):
        aux.append(ma[i][j]+mb[i][j])
    mrr.append(aux)
print("m1")
for a in matriz1:
    print(a)
print("m2")
for a in matriz2:
    print(a)
print("m3")
for a in matriz3:
    print(a)

print("suma m1 m2")
for a in ms:
    print(a)
print("resultado (a+b)*c")
for a in mr:
    print(a)
print("a*c+b*c")
for a in mrr:
    print(a)
