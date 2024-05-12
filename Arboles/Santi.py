# diseñe una funcion que genere 10  numeros aleatorios de dos cifras
import random
def num_alea():
    lista = []
    for i in range(0, 10):
        lista.append(random.randint(10, 99))
    return lista

lista = num_alea()

def promedio(l):
    suma = 0
    cont = 0
    for i in range(0, 10):
        if l[i] % 2 == 0:
            suma = suma + l[i]
            cont = cont + 1
            
    return suma / cont
print(lista)
print(promedio(lista))