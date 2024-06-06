"""
6.
En un arreglo de 10 posiciones se generan números aleatorios de 2 cifras, 
determinar:
a. Cantidad de números pares
b. Promedio de números impares
c. Posiciones donde hay números primos
d. Cantidad de números capicúas
e. Promedio de números compuestos (no son primos)
f. Posición del mayor
g. Posición de los dos menores
h. Promedio de números en posiciones impares
"""

import random 

arreglo = []
num_pares = 0
valor_impares = 0
cantidad_impares = 0
promedio_impares = 0
posiciones_num_primos = []
contador_divisores = 0 
acumulador_compuestos = 0
contador_compuestos = 0
mayor = -99
pos_mayor = 0
min1 = 99
min2 = 99
pos_min1 = -1
pos_min2 = -1
acumulador_pos_impares = 0
cantidad_pos_impares = 0

for i in range(0, 10):
    arreglo.append(random.randint(10,99))
    
# Pares
for i in range(0, 10):
    if arreglo[i] % 2 == 0:
        num_pares += 1

# Promedio impares
for i in range(0, 10):
    if arreglo[i] % 2 != 0:
        valor_impares += arreglo[i]
        cantidad_impares += 1
      
promedio_impares = valor_impares / cantidad_impares

# Primos y compuestos

for i in range(0, 10):
    contador_divisores = 0
    for j in range(1, arreglo[i]+1):
        if arreglo[i] % j == 0:
            contador_divisores += 1
    if contador_divisores == 2:
        posiciones_num_primos.append(i+1)
    else:
        acumulador_compuestos += arreglo[i]
        contador_compuestos += 1
        
# Capicuas 
str_numero = ''
str_numero_invertido = ''
capicua = 0
capicuas = []

for i in range(0, 10):
    str_numero = str(arreglo[i])
    str_numero_invertido = ''
    for j in range(-1, -3, -1):
        str_numero_invertido += str_numero[j]
    for j in range(0, 10):
        if i == j:
            pass
        elif arreglo[j] == int(str_numero_invertido):
            capicua += 1
            capicuas.append([arreglo[i], int(str_numero_invertido)])
        
        
# Mayor

for i in range(0, 10):
    if mayor <= arreglo[i]:
        mayor = arreglo[i]
        pos_mayor = i
        
# Menores

for i in range(0, len(arreglo)):
    if arreglo[i] < min1:
        min2 = min1
        pos_min2 = pos_min1
        min1 = arreglo[i]
        pos_min1 = i
    elif arreglo[i] < min2:
        min2 = arreglo[i]
        pos_min2 = i
        
# Promedio pos impares

for i in range(0, 10):
    if i % 2 != 0:
        acumulador_pos_impares += arreglo[i]
        cantidad_pos_impares += 1

    
        

print('Arreglo: ', arreglo)
print('Cantidad de numeros pares: ', num_pares)
print('Promedio de impares: ', promedio_impares)
print('Posiciones de primos: ', posiciones_num_primos)
print('Numeros Capicuas: ', capicua, capicuas)
print('Promedio numeros compuestos: ', acumulador_compuestos/contador_compuestos)
print('Posicion del numero mayor: ', pos_mayor+1)
print('Posicion de los dos numeros menores: 1. ', pos_min1+1, '2. ', pos_min2+1)
print('Promedio de numeros en posiciones impares: ', acumulador_pos_impares/cantidad_pos_impares)

