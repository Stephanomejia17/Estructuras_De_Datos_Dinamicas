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
def suma_de_numeros(lista, numero,visitados=[], k=-1,piso = 0,suma=0):
    if numero in lista:
        return True
    else:
        k+=1
        if piso < len(lista):
            if lista[k] not in visitados:
                visitados.append(lista[k])
                for i in range(0, len(visitados)):
                    suma += visitados[i]
                if suma == numero:
                    return True
                else:
                    if len(visitados) != len(lista):
                        return suma_de_numeros(lista, numero, visitados, k, suma=0)
                    else:
                        visitados.remove(visitados[-1])
                        return suma_de_numeros(lista, numero, visitados,k, suma=0)
        else:
            visitados.remove(visitados[-1])
            piso -= 1
            return suma_de_numeros(lista,numero, visitados, k, suma=0)

print(suma_de_numeros(l, 9))
    
        
    

