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
        
class DNode:
    def __init__(self, value = None, next = None, prev = None) -> None:
        self.value = value
        self.next: Node = next
        self.prev: Node = prev
    def __str__(self) -> str:
        return f"{self.value}"
    def getNext(self):
        return self.next
    def getValue(self):
        return self.value
    def setNext(self, next):
        self.next = next
    def setValue(self, value):
        self.value = value
        
class DLinkedList:
    def __init__(self) -> None:
        self.head: DNode = None
        self.tail: DNode = None
        self.size = 0
        
    def append(self, node, e): #Agregar nodos al final de la lista
        if self.head == None:
            self.head = DNode(e)
            self.tail = self.head
            self.size += 1
            return 
        if node.next == None:
            new_node = DNode(e)
            node.next = new_node
            self.tail = new_node
            self.tail.prev = node
            self.size += 1
            return 
        self.append(node.next, e)
    def preppend(self, e): # Añadir nodos al comienzo
        if self.head is not None:
            new_node = DNode(e)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = DNode(e)
        
    def delete_at_index(self, index): # Eliminar nodos en un indice dado
        if index > self.size - 1: 
            return 
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        
        elif index > 0:
            pos = 0
            node = self.head
            if index == self.size-1:
                self.tail = self.tail.prev
                self.tail.next.prev = None
                self.tail.next = None
            else:  
                while pos != index - 1:
                    node = node.next
                    pos += 1
                aux_node = node.next.next
                aux_node.prev = node
                node.next.next = None
                node.next.prev = None
                node.next = aux_node
    def getSize(self):
        return self.size
            
def traverse(Node): # Imprimir la lista
        while Node != None:
            print(Node.getValue())
            Node = Node.getNext()   
            
def ordenarListas(l1: DLinkedList, l2: DLinkedList):
    aux_headl1 = l1.head
    aux_headl2 = l2.head
    if l2.head.next == None:
        return
    if l1.head.next == None:
        ordenarListas(aux_headl1, l2.head.next)
    else:
        if l2.head.value <= l1.head.value:
            if l1.head.prev == None:
                l1.head.prev = l2
                l2.head.next = l1
            elif l1.head.next == None:
                l1.head.next = l2
                l2.head.prev = l1
            else:
                pass
        
              
            
dn1 = DNode()
dn2 = DNode()




dn3 = DNode()
dn4 = DNode()

dll1 = DLinkedList()
dll1.append(dll1.head, 4)
dll1.append(dll1.head, 5)
dll1.append(dll1.head, 25)


# 0.3
def rotate(dll: DLinkedList, n):
    for i in range(n):
        dll.head.prev = dll.tail
        dll.tail.prev.next = None
        dll.tail = dll.tail.prev
        dll.head.prev.prev = None
        dll.head.prev.next = dll.head
        dll.head = dll.head.prev
        
   
#0.2
def rotate_rec(dll: DLinkedList, n):
    if n == 0:
        return
    else:
        dll.head.prev = dll.tail
        dll.tail.prev.next = None
        dll.tail = dll.tail.prev
        dll.head.prev.prev = None
        dll.head.prev.next = dll.head
        dll.head = dll.head.prev
        rotate_rec(dll, n-1)    


#0.5    
def buquedad_y_elim_de_numeros(dll: DNode, conf = False):
    if dll is None:
        return
    else:
        if dll.prev != None and dll.next != None:
            if dll.getValue() > dll.prev.getValue() and dll.getValue() < dll.next.getValue():
                dll.prev.next = dll.next
                dll.next.prev = dll.prev
                conf = True
                dll.prev = None
        
        buquedad_y_elim_de_numeros(dll.next)
        if conf == True:
            dll.next = None
               
               
"""
E2. Cree una función que reciba dos listas enlazadas representando números. Devuelva una lista enlazada con el 
resultado de la suma de estos números.

Cada lista enlazada representa el número invertido.
El resultado debe representar el resultado en una lista enlazada donde cada nodo representa un dígito del número.
"""

# 0.4
def suma_de_nodos(dll: DNode, dll2: DNode, c = 0, res = DLinkedList()):
    if dll.next is None or dll2.next is None:
        restante = (dll.getValue() + dll2.getValue()) % 10
        res.append(res.head, restante + c)
        return res
    else:
        restante = (dll.getValue() + dll2.getValue()) % 10
        if dll.getValue() + dll2.getValue() >= 10:
            c = 0
            aux_c = 1
            res.append(res.head, restante + c)
        else:
            c = (dll.getValue() + dll2.getValue())//10
            aux_c = c
            res.append(res.head, restante + c)
            
            
        
        return suma_de_nodos(dll.next, dll2.next, aux_c, res)


def suma_de_nodos_der(dll: DNode, dll2: DNode, c = 0, res = DLinkedList()):
    if dll.prev is None or dll2.prev is None:
        restante = (dll.getValue() + dll2.getValue()) % 10
        res.preppend(restante + c)
        return res
    else:
        
        restante = (dll.getValue() + dll2.getValue()) % 10 # 1
        
        if dll.getValue() + dll2.getValue() >= 10:
            c = 0
            aux_c = 1
        else:
            c = (dll.getValue() + dll2.getValue())//10
            aux_c = c
            
            
        res.preppend(restante + c)  
        return suma_de_nodos(dll.prev, dll2.prev, aux_c, res)
    
dll = DLinkedList()
dll.append(dll.head, 5)
dll.append(dll.head, 1)
dll.append(dll.head, 8)

dll4 = DLinkedList()
dll4.append(dll4.head, 9)
dll4.append(dll4.head, 6)
dll4.append(dll4.head, 7)
dll4.append(dll4.head, 8)

resultante = DLinkedList()


resultante = suma_de_nodos_der(dll.tail, dll4.tail)

traverse(resultante.head)