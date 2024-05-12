"""
Tiene nodos y enlaces, estas pueden gestionar cualquier tipo de datos y tener cualquier tamaño.

cada nodo tiene dos cosas: un valor y el enlace (dirección de memoria)    
"""
# 0.2
class Node:
    def __init__(self, value = None, next = None) -> None:
        self.value = value
        self.next = next
    def getNext(self):
        return self.next
    def getValue(self):
        return self.value
    def setNext(self, next):
        self.next = next
    def setValue(self, value):
        self.value = value
    
H = Node("H")
O = Node("O")
L = Node("L")
A = Node("A")

H.setNext(O)
O.setNext(L)
L.setNext(A)

#0.2
def recorrer(punto_partida: Node):
    while punto_partida != None:
        print(punto_partida.getValue())
        punto_partida = punto_partida.getNext()
      
# 0.2  
def recorrerRecursion(punto_partida: Node):
    if punto_partida == None:
        return
    else:
        print(punto_partida.getValue())
        recorrerRecursion(punto_partida=punto_partida.getNext())

# 0.3
def pegarValorAlFinalDeLaLista(punto_partida: Node, value):
    nuevo_nodo = Node(value=value)
    while punto_partida.getNext() != None:
        punto_partida = punto_partida.getNext()
    punto_partida.setNext(nuevo_nodo)
        
        
def pegarValorAlFinalDeLaListaRecusivo(punto_partida: Node, value):
    nuevo_nodo = Node(value=value)
    if punto_partida.getNext() == None:
        punto_partida.setNext(nuevo_nodo)
    else:
        pegarValorAlFinalDeLaListaRecusivo(punto_partida=punto_partida.getNext(), value=value)
        
# 0.5
def insertarElementos(punto_partida: Node, posicion: int, value):
    cont = 0
    nuevo_nodo = Node(value=value)
    while posicion != cont:
        punto_partida = punto_partida.getNext()
        cont += 1
    nuevo_nodo.setNext(punto_partida.getNext())    
    punto_partida.setNext(nuevo_nodo)

    
def insertarElementosRecursivo(punto_partida: Node, posicion:int, value, cont=0):
    nuevo_nodo = Node(value=value)
    if posicion == cont:
        nuevo_nodo.setNext(punto_partida.getNext())
        punto_partida.setNext(nuevo_nodo)
        return
    else:
        insertarElementosRecursivo(punto_partida=punto_partida.getNext(), posicion=posicion, value=value, cont=cont+1)
    
    
    
#0.5
def eliminarElementosRecursivo(punto_partida: Node, valor, cont = 0, nodo_anterior=None):
    if punto_partida.getValue() == valor:
        nodo_anterior.setNext(punto_partida.getNext())
        return
    else:
        nodo_anterior = punto_partida
        eliminarElementosRecursivo(punto_partida=punto_partida.getNext(), valor=valor, cont=cont+1, nodo_anterior=nodo_anterior)
    
        

def invertirLista(punto_partida: Node, nodo_anterior=None):
    if punto_partida.getNext() == None:
        punto_partida.setNext(nodo_anterior)
        return
    else:
        invertirLista(punto_partida=punto_partida.getNext(), nodo_anterior=punto_partida)
        punto_partida.setNext(nodo_anterior)
    
        
class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.size = 0
        
    def traverse(self): # Imprimir la lista
        while self.head != None:
            print(self.head.getValue())
            self.head = self.head.getNext()
        
    def append(self, node, e): #Agregar nodos al final de la lista
        if self.head == None:
            self.head = Node(e)
            self.size += 1
            return 
        if node.next == None:
            new_node = Node(e)
            node.next = new_node
            self.size += 1
            return 
        self.append(node.next, e)
    def preppend(self, e): # Añadir nodos al comienzo
        new_node = Node(e)
        new_node.next = self.head
        self.head = new_node
        
    def delete_at_index(self, index): # Eliminar nodos en un indice dado
        if index > self.size - 1: 
            return 
        if index == 0:
            self.head = self.head.next
        else:
            pos = 0
            node = self.head
            while pos != index - 1:
                node = node.next
                pos += 1
            aux_node = node.next.next
            node.next.next = None
            node.next = aux_node
                 
                 
# Mas bombas o mas rango

# 1 espacio por turno
class LinkedMatrix:
    def __init__(self, value: None) -> None:
        self.value: LinkedList = value
        self.next: LinkedList = None
    
    def append(self, e: LinkedList):
        self.next = e
    
ll = LinkedList()
ll1 = LinkedList()
lm = LinkedMatrix(ll)
lm = LinkedMatrix(ll1)

