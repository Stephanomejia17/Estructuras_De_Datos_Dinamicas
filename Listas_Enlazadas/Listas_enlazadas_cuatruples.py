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
    def __init__(self, value = None, east = None, west = None, north = None, south = None) -> None:
        self.value = value
        self.east: Node = east
        self.west: Node = west
        self.north: Node = north
        self.south: Node = south
    def __str__(self) -> str:
        return f"{self.value}"
    
    # Getters
    def getEast(self):
        return self.east
    def getWest(self):
        return self.west
    def getNorth(self):
        return self.north
    def getSouth(self):
        return self.south
    def getValue(self):
        return self.value
    # Setters
    def setEast(self, next):
        self.east = next
    def setValue(self, value):
        self.value = value
    def setNorth(self, north):
        self.north =  north
    def setSouth(self, south):
        self.south = south
        
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
        if node.east == None:
            new_node = DNode(e)
            node.east = new_node
            self.tail = new_node
            self.tail.prev = node
            self.size += 1
            return 
        self.append(node.east, e)
    def preppend(self, e): # Añadir nodos al comienzo
        new_node = DNode(e)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        
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
            
def aplanar_lista(dll: DLinkedList, dll_res: DLinkedList = DLinkedList(), cont = 0):
    if cont == 0:
        dll_head = dll.head
    if dll_head.east == None:
        return dll_res
    else:
        cont += 1
        if dll_head.south == None:
            dll_res.append(dll_head, dll_head.value)
        else:
            # saltar al south
            dll_res.append(dll_head.south, dll_head.south.value)
        aplanar_lista(dll_head.east, dll_res, cont)
        dll_res.append(dll_head.east, dll_head.east.value)
 

dll2 = DLinkedList()

node1 = DNode()
node2 = DNode()
node3 = DNode()
node4 = DNode()
node5 = DNode()
node6 = DNode()
node7 = DNode()
node8 = DNode()
node9 = DNode()
node10 = DNode()
node11 = DNode()


node1.east = node2
node2.east = node3
node2.south = node4
node4.east = node5
node5.east = node6
node6.east = node7
node6.south = node8
node8.east = node9
node9.south = node10
node10.east = node11
    
dll2.head = node1
dll2.tail = node11

print(aplanar_lista(dll2))


def insert(dll1: DLinkedList, dll2: DLinkedList, v, dll1_head: DNode = None, dll2_head: DNode = None, cont = 0):
    if cont == 0:
        dll1_head = dll1.head
        dll2_head = dll2.head
    if dll1_head.value == v:
        dll1_head.south = dll2_head
        return 
    else:
        cont += 1
        insert(dll1, dll2, v, dll1_head.east, dll2_head.east, cont)
    