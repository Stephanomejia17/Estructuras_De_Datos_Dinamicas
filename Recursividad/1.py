# Recursividad es una función que se llama a sí misma directa o indirectamente

""" La funcones recursivas tienen dos casos
        Caso Recursivo: llamado recursivo, llamado a la funcion
        
        Caso Base: Caso Parada, usualmente se usa un condicional acompañado de un return


"""
def factorial(n):
    # Caso Base
    if n == 1:
        return 1
    
    # Caso Recursivo
    return n * factorial(n-1)
        

def num_uno_a_cien(n):
    if n == 10:
        print(10)
    else:
        print(n)
        num_uno_a_cien(n+1)
    
def cien_a_num(n):
    if n == 10:
        print(10)
    else:
        num_uno_a_cien(n+1)
        print(n)
        
            
l = [2,2,1,1,34,42,5,234,1,4]

def count1(lista, c=0):
    if len(lista) == 0:
        return c
    else:
        if lista[0] == 1:
            return count1(lista[1:], c+1)
        else:
            return count1(lista[1:], c)
        
            
def elim_numero(lista, n=2):
    if len(lista) == 0:
        return lista
    else:
        if lista[0] == n:
            lista.remove(n)
            return elim_numero(lista)
        else:
            return elim_numero(lista[1:], n)
        
        
def mayor(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        mayor_numero = lista[0]
        m = mayor(lista[1:])
        if mayor_numero >= m:
            return mayor_numero
        else:
            mayor_numero = m
            return mayor_numero

# Preguntar como hacerlo
# Problema: replicar n veces cada elemento de una lista dada con recursividad
            
def replicar_valores_de_lista(lista, n):
    if len(lista) == 1:
        return lista, lista[0]
    else:
        lista, value = replicar_valores_de_lista(lista[1:], n)
        
        for i in range(0, n):
            lista.insert(1,value)
    

def multiplicar(N1, N2, res=0):
    if N2 == 0:
        return N2
    else:
        if N2 >= 0:
            return N1 + multiplicar(N1, N2-1, res)
        else:
            return multiplicar(N1, N2+1, res) - N1
        
#print(multiplicar(2,-5))


def multiplicar_2(N1, N2, res=0):
    if N2 == 0:
        return res
    else:
        if N2 >= 0:
            return multiplicar_2(N1, N2-1, res+N1)
        else:
            return multiplicar_2(N1, N2+1, res-N1)
        
#print(multiplicar_2(2,-10))
    

lista = [1,1,1,2,3,3,2,2,4,4]

def contador_de_elemetos(lista, res={}):
    if len(lista) == 0:
        return res
    else:
        if lista[0] in res.keys():
            res[lista[0]] += 1
            return contador_de_elemetos(lista[1:], res)
        else:
            res[lista[0]] = 1
            return contador_de_elemetos(lista[1:], res)
        
#print(contador_de_elemetos(lista))      
    
matriz = [[1,2,3], [4,5,6], [7,8,9]]

def buscador_en_matriz(matriz, n, res={}, i=0, j=0):
    if i == (len(matriz)):
        return res
    else:
        if j == (len(matriz)):
            buscador_en_matriz(matriz, n, res, i+1, j=0)
            return res
        else:
            if matriz[i][j] == n:
                res[i] = j
            else:
                buscador_en_matriz(matriz,n,res,i,j+1)
                return res
                

def strings_repetidos(enunciado, res={}):
    if len(enunciado) == 0:
        return res
    else:
        if enunciado[0] in res.keys():
            res[enunciado[0]] += 1
            strings_repetidos(enunciado[1:], res)
        else:
            res[enunciado[0]] = 1
            strings_repetidos(enunciado[1:], res)
        try:
            if res[enunciado[0]] > 1:
                del res[enunciado[0]]
                return res
        except:
            return res
        return res
    
def strings_repetidos2(enunciado, res={}, i=0):
    if i < len(enunciado):
        return False
    else:
        if enunciado[0] in res.keys():
            
            return True
        else:
            res[enunciado[0]] = 1
            return strings_repetidos2(enunciado[i+1], res)


def strings_repetidos3(enunciado, res={},i=0):
    if i>len(enunciado):
        mayor = enunciado[0]
        return res
    else:
        if enunciado[0] in res.keys():
            res[enunciado[0]] += 1
            strings_repetidos3(enunciado[1:], res)
        else:
            res[enunciado[0]] = 1
            strings_repetidos3(enunciado[1:], res)
        
        if res[enunciado[0]] > mayor:
            mayor = res[enunciado[0]]
            
            return mayor
        
l = [2,4,5]
def suma_de_numeros(lista, numero,visitados=[], i=0,suma=0, no_pasar=[], k=0):
    if numero in lista:
        return True
    if i == len(lista):
        return False
    else:
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> Laptop
        k += 1
        visitados.append([])
        if k < len(lista):
            if lista[k] not in visitados[piso]:
                visitados[piso].append(lista[k])
                for i in range(0, len(visitados[piso])):
                    suma += visitados[piso][i]
                if suma == numero:
                    return True
                else:
                    if len(visitados[piso]) != len(lista):
                        return suma_de_numeros(lista, numero, visitados, k, piso, suma=0)
                    else:
                        return suma_de_numeros(lista, numero, visitados, piso=piso, k=0,suma=0)
        else:
            piso += 1
            visitados.append([])
            return suma_de_numeros(lista,numero, visitados, k, piso,suma=0)
<<<<<<< HEAD
=======
=======
        if lista[i] in no_pasar:
            visitados = visitados[:len(visitados)-1]
            return False
        elif lista[i] not in visitados:
            visitados.append(lista[i])
            no_pasar.append(lista[i])
        for j in range(0, len(visitados)):
            suma += visitados[j]
        if suma == numero:
            return True
        else:
            if not(suma_de_numeros(lista, numero, visitados, i+1, suma=0, no_pasar=no_pasar,k=k) or suma_de_numeros(lista, numero, visitados[:len(visitados)-1], i+1, suma=0, no_pasar=no_pasar,k=k)):
                k += 1
                return suma_de_numeros(lista,numero,visitados=[],i=k,suma=0,no_pasar=[],k=k)
            else:
                return True

print(suma_de_numeros(l, 9))

n = [1,4,3,2,7,5,9]
def busqueda(lista, numero, j, i=0):
    mid = len(lista)//2
    if i > mid or mid > j:
        return False
    if lista[i] == numero or lista[j] == numero:
        return True
    else:
        return busqueda(lista, numero, i=i+1, j=j) or busqueda(lista, numero, j=j-1, i=i)
    
>>>>>>> 9169697b66ead6d7d5cf6f276febfb3d6e99fad8
>>>>>>> Laptop
        

#print(suma_de_numeros(l, 6))

lista_de_busqueda = [1,10,15,90,101]
def busqueda(lista, numero,j = 0,i = 0):
    mid = (i+j)//2
    j = len(lista)-1
    if lista[mid] == numero:
        return True
    else:
        if lista[mid] > numero:
            j = mid - 1
            return busqueda(lista, numero, i, j)
        else:
            i = mid + 1
            return busqueda(lista, numero, i, j)
    return False
        
#print(busqueda(lista_de_busqueda, 14))

lista_de_busqueda = [1,10,15,90,101]

def rec_binaria(lista, numero, i=0,j=0):
    j = len(lista) - 1
    if i == j:
        return False
    if lista[i] == numero or lista[j] == numero:
        return True
    else:
        
        return rec_binaria(lista, numero, i+1, j) or rec_binaria(lista, numero, i=0, j=j-1)
        
        
        
 
 
"""
E1. Cree una función recursiva de cola que reciba un entero y retorne 
cuántos dígitos de este número son múltiplos de 2 y de 4. Ignore el cero.

Por ejemplo: si la función recibe el número 34523, deberá retornar 1 
ya que hay sólo un número que es múltiplo de ambos números (el 4).
"""   
def e1(numero, res=0, numero_prov=0):
    if numero < 1:
        return res
    else:
        numero_prov = numero % 10
        if numero_prov == 0:
            return e1(numero=(numero//10), res=res, numero_prov=0)
        elif (numero_prov % 2) == 0 and (numero_prov%4) == 0:
            res += 1
            return e1(numero=(numero//10), res=res, numero_prov=0)
        else:
            return e1(numero=(numero//10), res=res, numero_prov=0)
            
# assert(e1(12345) == 1)
# assert(e1(3338883) == 3)
# assert(e1(353535) == 0)
# assert(e1(1908) == 1)

"""
E2. Cree una función no recursiva de cola que invierta sólo la segunda mitad de un string.

Por ejemplo, si la función recibe "Hola", deberá retornar "Hoal".
Asuma que el punto medio es tamaño//2
"""

def e2(palabra, mitad=0, i=0, j=-1,res=""):
    mitad = len(palabra)//2
    if len(res) == len(palabra):
        return res
    if palabra == "":
        return res
    else:
        if i < mitad:
            res += palabra[i]
            return e2(palabra, mitad, i=i+1, j=j, res=res)
        else:
            res += palabra[j]
            return e2(palabra, mitad,i,j=j-1, res=res)
            

#casos de prueba
# assert(e2("") == "")
# assert(e2("hola") == "hoal")
# assert(e2("ay muchachos!") == "ay muc!sohcah")
# assert(e2("Estructuras") == "Estrusarutc")     

def e2(palabra, mitad=0, i=0, j=0,res=""):
    mitad = len(palabra)//2
    if palabra == "":
        return res
    else:
        if j > -(mitad):
            res += palabra[j]
            return res + e2(palabra, mitad, i, j=j-1, res=res) + e2(palabra, mitad, i=i+1, j=j, res=res)
            
            
            
        
            

#casos de prueba
#assert(e2("") == "")
#assert(e2("hola") == "hoal")
#assert(e2("ay muchachos!") == "ay muc!sohcah")
#assert(e2("Estructuras") == "Estrusarutc")   
        
""" 
E3. Cree una función recursiva de cola que calcule la sumatoria de todos los números impares de una matriz nxn.

Por ejemplo, si la función recibe la matriz m = [[1,2],[3,4]], deberá retornar 4 porque los únicos números impares de esta matriz son 1 y 3.
"""        
def e3(matriz, i = 0, j = 0, res=0):
    if i>len(matriz) and j > len(matriz[i]):
        return res
    else:
        if matriz[i][j] % 2 != 0:
            res += matriz[i][j]
            return e3(matriz, i, j=j+1, res=res)
        else:
            return e3(matriz, i, j=j+1, res=res)

#casos de prueba
#assert(e3([]) == 0)
#assert(e3([[1,2,3,4],[1,2,3,4],[5,6,7,8],[1,1,1,1]]) == 24)
#assert(e3([[1,1,1],[0,0,0],[1,1,1]]) == 6)
#assert(e3([[2,2],[0,0]]) == 0)
    
""" 
E4. Cree una función recursiva que reciba una lista "l", un elemento "e" y un índice "i" y que retorne si el elemento "e" está en la lista "l" en la posición "i".

Por ejemplo, si recibe la lista l = [1,2,3], e=2 y i=0, debería retornar False porque en la posición 0 de l no hay un 2.
Nota: en este ejemplo se tendrá en cuenta el procedimiento para evitar que retornen False siempre y que pasen tres casos de prueba automáticamente.
"""
def e4(lista, elemento, i, j=0):
    if elemento not in lista:
        return False
    if j == len(lista):
        return False
    else:
        if i == j and elemento == lista[j]:
            return True
        else:
            return e4(lista, elemento, i, j=j+1)
#casos de prueba
#assert(e4([1,2,3],2,0) == False)
#assert(e4([1,1,1,1,1],2,1) == False)
#assert(e4([0,0,1,1],0,1) == True)
#assert(e4([],2,0) == False)


m = [[6,[[5,[[3,[[[1,[[]]]],8]]]]]]]
def e6(matriz, elemento, i=0, k=0):
    if i >= len(matriz):
        return k
    else:
        if elemento in matriz:
            return k
        elif type(matriz[i]) is list:
            k+=1
            return e6(matriz[i], elemento, i=0,k=k) 
        else:
            i+=1
            return e6(matriz, elemento, i,k)
        
print(e6(m, 5))