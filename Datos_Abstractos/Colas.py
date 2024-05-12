import random
"""
Cola:

- Enqueue (e): Agregar elemento elemento a la cola
- Dequeue (): Elimina el primer elemento que entró y lo retorna (Solo con listas con elementos)
- First (): retornar el primero que entró a la cola (Solo con listas con elementos)
"""

class ColaSinElementos(Exception):
    def __init__(self, *args: object) -> None:
        mensaje = "La cola no tiene elementos..."
        super().__init__(mensaje)

class PilaVacia(Exception):
    def __init__(self) -> None:
        mensaje: str = "La pila está vacía"
        super().__init__(mensaje)
        
class LimiteDePila(Exception):
    def __init__(self) -> None:
        mensaje: str = "La pila no puede almacenar más valores"
        super().__init__(mensaje)

class Stack:
    
    def __init__(self) -> None:
        self.stack: list = []
    def __str__(self) -> str:
        return f"{self.stack}"
    
    def push(self, valor) -> None:
        self.stack.append(valor)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        raise PilaVacia
    
    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        raise PilaVacia
    
    def _limite(self):
        if len(self.stack) >= self.tamaño:
            raise LimiteDePila
        return True
    def getTamanho(self):
        return len(self.stack)
            
class Cola:
    cola: list[int]
    def __init__(self) -> None:
        self.cola: list[int] = []
    def __str__(self) -> str:
        return f"{self.cola}"
    def enqueue(self, valor):
        self.cola.insert(0, valor)
    def dequeue(self):
        return self.cola.pop()
    def first(self):
        return self.cola[-1]
    def getTamaño(self):
        return len(self.cola)
    def setCola(self, cola_prov):
        self.cola = cola_prov

# Implementar
    
class ColaConPila():
    def __init__(self, tamaño) -> None:
        self.stack: Stack = Stack(tamaño)
        self.stack_invertido: Stack = Stack(tamaño)
        self.tamaño = tamaño
        self.lista: list = []
    def __str__(self) -> str:
        return f"{self.stack.stack}"
    def enqueue(self, valor):
        self.stack.push(valor)
    def dequeue(self):
        for i in range(self.tamaño):    
            self.stack_invertido.push(self.stack.pop())
        res = self.stack_invertido.pop()
        for i in range(self.tamaño):
            self.stack.push(self.stack_invertido.pop())
        self.stack.pop()
        return res
    def first(self):
        pass
    def invertir(self):
        for i in range(self.tamaño):
            self.stack_invertido.push(self.stack.pop())


class ColaLlena(Exception):
    def __init__(self) -> None:
        mensaje: str = "La cola esta llena"
        super().__init__(mensaje)
class ColaVacia(Exception):
    def __init__(self) -> None:
        mensaje: str = "La cola esta vacia"
        super().__init__(mensaje)
    

class ColaEstatica():
    def __init__(self, tamanho) -> None:
        self.cola = [None for i in range(0, tamanho)]
        self.tamanho = tamanho
        self.contador_espacio = 0
        self.__idx_enqueue = 0
        self.__idx_dequeue = 0
    def __str__(self) -> str:
        return f"{self.cola}"
    def enqueue(self, valor: int):
            
        if self.contador_espacio == self.tamanho:
            raise ColaLlena
        else:
            self.cola[self.__idx_enqueue] = valor
            self.contador_espacio += 1
        
        
        self.__idx_enqueue = self.size(self.__idx_enqueue)
        
    def dequeue(self):
        if self.contador_espacio == 0:
            raise ColaVacia
        else:
            m = self.cola[self.__idx_dequeue]
            self.cola[self.__idx_dequeue] = None
            self.contador_espacio -= 1
            self.__idx_dequeue = self.size(self.__idx_dequeue)
        
        
        
        return m
    def first(self):
        if self.contador_espacio == 0:
            raise ColaVacia
        return self.cola[self.__idx_dequeue]
    def size(self, idx):
        if idx == self.tamanho-1:
            idx = 0
        else:
            idx += 1
        return idx
            
class Persona:
    def __init__(self, nombre: str,edad: int,peso: int) -> None:
        self.edad: int = edad
        self.nombre: str = nombre
        self.peso = peso
    def __str__(self) -> str:
        return f"{self.nombre}, {self.edad}, {self.peso} "
        
    def __str__(self) -> str:
        return f"{self.nombre}, {self.edad}"
    def getEdad(self) -> int:
        return self.edad
    def getNombre(self) -> str:
        return self.nombre
    def getPeso(self):
        return self.peso

class ColaDePrioridad:
    def __init__(self) -> None:
        self.cola = []
    def __str__(self) -> str:
        return f"{self.cola}"
    def enqueue(self, persona: Persona):
        self.cola.append(persona)
    def dequeue(self):
        self.__ordenar()
        return self.cola.pop()
        
    def first(self):
        self.__ordenar()
        return self.cola[-1]
    def __ordenarEdad(self):
        # Insertion sort
        for i in range(len(self.cola)):
            edad = self.cola[i]
            idx = i - 1 
            while idx >= 0 and edad.getEdad() < self.cola[idx].getEdad():
                self.cola[idx + 1] = self.cola[idx]
                idx -= 1
            self.cola[idx + 1] = edad
    def __ordenarPeso(self):
        # Insertion sort
        for i in range(len(self.cola)):
            peso = self.cola[i]
            idx = i - 1 
            while idx >= 0 and peso.getPeso() < self.cola[idx].getPeso():
                self.cola[idx + 1] = self.cola[idx]
                idx -= 1
            self.cola[idx + 1] = peso

""" 
c = ColaDePrioridad()
p1 = Persona("Juan", 15)
p2 = Persona("Margot", 54)
p3 = Persona("Nathy", 19)
p4 = Persona("Agusto", 54)
p5 = Persona("Pedro", 48)

c.enqueue(p1)
c.enqueue(p2)
c.enqueue(p3)
c.enqueue(p4)
c.enqueue(p5)

print(c.dequeue())
print(c.dequeue())
"""

def invertirCola(cola: Cola, prov = 0) -> Cola:
    if cola.getTamaño() == 0:
        return prov
    else:
        prov = cola.dequeue()
        invertirCola(cola, prov)
        cola.enqueue(prov)
    return cola
    
        
def invertirColaConColas0(cola: Cola) -> Cola:
    cola_res: Cola = Cola()
    cola_prov: Cola = cola
    idx = 0
    for i in range(cola.getTamaño()):
        cola_prov = cola
        for j in range(cola.getTamaño() - idx):
            value_prov = cola_prov.dequeue()
        cola_res.enqueue(value_prov)
        idx += 1
        
    return cola_res

def invertirColaConColas(cola: Cola) -> Cola:
    idx = 2
    cola_prov = Cola()
    cola_res = Cola()
    for i in range(cola.getTamaño()):
        for j in range(cola.getTamaño() - idx):
            cola_prov.enqueue(cola.dequeue())
        
        cola_res.enqueue(cola.dequeue())
        idx += 1

"""
SIMULACRO
E1. Cree una función que reciba una pila y determine 
si sus elementos están ordenados ascendentemente desde 
el tope. Asuma que en la pila sólo hay números enteros
"""
        
def pila_ordenados(pila: Stack):
    pila_prov = Stack()
    res: bool = True
    for i in range(pila.getTamanho()-1):
        value = pila.pop()
        pila_prov.push(value)
        if value > pila.top():
            res = False
            break

    for i in range(pila_prov.getTamanho()):
        pila.push(pila_prov.pop())
    
    return res
            
        

"""
E2. Existe un listado de personas con nombre, estatura (en metros) y peso (en kilogramos) de aproximadamente 1000 datos. 
Su tarea, es atender lotes de a 50 personas y escoger a la persona con menor índice corporal por lote. Imprima por lote 
el nombre y el índice de masa corporal.

Defina cuál estructura es más adecuada para atender el problema y haga la implementación necesaria.
"""


"""E3. Dada una cola llena de pilas y un elemento E, determine si alguna de estas pilas contiene el elemento E. Asegúrese 
de mantener la integridad de la cola y las pilas, es decir, al final del proceso, tanto las colas como las pilas deben 
quedar intactas.

Sólo puede usar colas y pilas como colecciones para la solución
"""

def busqueda(cola, E):
    cola_prov = Cola()
    res = False
    for i in range(cola_prov.getTamaño()):
        pila_prov = Stack()
        for j in range(cola.First().getTamanho()):
            pila_prov.push(cola.First().Top())
            if cola.First().pop() == E:
                res = True
                print(pila_prov)
                break

        
    return res


"""
E4. Dada una pila llena de colas llenas de caracteres, determine si con los caracteres de estas colas 
se puede formar el string S. Cree una función que reciba esta pila y devuelva True o False con base en la respuesta.
"""

pila = Stack()

a = Cola()
b = Cola()
c = Cola()
d = Cola()
e = Cola()

a.enqueue("A")
a.enqueue("B")

b.enqueue("H")
b.enqueue("D")

c.enqueue("E")
c.enqueue("F")

d.enqueue("G")
d.enqueue("A")

e.enqueue("H")
e.enqueue("H")
e.enqueue("H")

pila.push(a)
pila.push(b)
pila.push(c)
pila.push(d)
pila.push(e)

print(pila)
print("a: ", a)
print("b: ",b)
print("c: ",c)
print("d: ",d)
print("e: ",e)


def construirString(pila: Stack, palabra):
    res = False
    cont = 0
    pila_prov = Stack()
    cola_prov = Cola()
    
    for i in range(pila.getTamanho()):
        for j in range(pila.top().getTamaño()):
            cola_prov.enqueue(pila.top().first())
            aux = pila.top().dequeue()
            if aux in palabra:
                res = True
                palabra = palabra[cont:]
                cont += 1
                break
            elif cont == len(palabra):
                res = False
                break
            cont += 1
        for k in range(cola_prov.getTamaño()):
            pila.top().enqueue(cola_prov.dequeue())
        pila_prov.push(pila.pop())
        
    for i in range(pila_prov.getTamanho()):
        pila.push(pila_prov.pop())
    return res
            
    

print(construirString(pila, "HHHH"))

print(pila)
print("a: ", a)
print("b: ",b)
print("c: ",c)
print("d: ",d)
print("e: ",e)
