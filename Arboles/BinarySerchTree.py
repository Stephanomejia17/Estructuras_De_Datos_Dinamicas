class Node:
    def __init__(self, value  = None, right_child = None, left_child = None) -> None:
        self.value = value
        self.left_child: Node = left_child
        self.right_child: Node = right_child
    def __str__(self) -> str:
        return f"Value: {self.value}, Left Child: {self.left_child}, Right Child: {self.right_child}"
    def setValue(self, value):
        self.value = value
    
    def setLeftChild(self, value):
        self.left_child = value
    def setRightChild(self, value):
        self.right_child = value
        
class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node = None
    
    def insert(self, value, root: Node):
        aux_root: Node = root
        if self.root == None:
            self.root = Node(value)
        elif aux_root.value < value:
            if aux_root.right_child is None:
                aux_root.right_child =  Node(value)
            else:
                self.insert(value, root = aux_root.right_child)
        elif aux_root.value > value:
            if aux_root.left_child is None:
                aux_root.left_child =  Node(value)
            else:
                self.insert(value, root = aux_root.left_child)
        else:
            return
        
    def may_men(self):
        aux_root: Node = self.root
        menor = None
        mayor = None
        while True:
            if aux_root.left_child is None:
                menor = aux_root.value
                break
            else:
                aux_root = aux_root.left_child
        aux_root = self.root
        while True:
            if aux_root.right_child is None:
                mayor = aux_root.value
                break
            else:
                aux_root = aux_root.right_child
                
        return menor, mayor
    
    def may_men_recursivo(self, aux_root = None, aux_root1 = None, mayor = None, menor = None):
        if aux_root is None or aux_root1 is None:
            aux_root = self.root
            aux_root1 = self.root
        if mayor is not None and menor is not None:
            return mayor, menor
        else:
            if aux_root.left_child is None:
                menor = aux_root.value
                return mayor, menor
            elif menor is None:
                mayor, menor = self.may_men_recursivo(aux_root=aux_root.left_child, aux_root1=aux_root1, mayor=mayor, menor=menor)
            if aux_root1.right_child is None:
                mayor = aux_root1.value
                return mayor, menor
            elif mayor is None:
                mayor, menor = self.may_men_recursivo(aux_root=aux_root, aux_root1=aux_root1.right_child, mayor=mayor, menor=menor)
                return mayor, menor
            return mayor, menor
        
    
# 0.7
    def triangulos(self, aux_root = None, cont = 0, izq = 0, der = 0):
        if aux_root is None:
            aux_root = self.root
        if aux_root.left_child is None and aux_root.right_child is None:
            return cont
        else:
            if aux_root.left_child is not None:
                izq = aux_root.left_child.value
            else:
                izq = 0
            if aux_root.right_child is not None:
                der = aux_root.right_child.value
            else: 
                der = 0
            if (aux_root.value + izq + der)%2 == 0:
                cont += 1
            if aux_root.left_child is not None:
                return self.triangulos(aux_root=aux_root.left_child, cont=cont, izq=izq, der=der)
            elif aux_root.right_child is not None:
                return self.triangulos(aux_root=aux_root.right_child, cont=cont, izq=izq, der=der)
        

    def print(self, node, prefix="", is_left=True):
        if not node:
            print("Empty Tree")
            return
        if node.right_child:
            self.print(node.right_child, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left_child:
            self.print(node.left_child, prefix + ("    " if is_left else "│   "), True)
            
bt = BinarySearchTree()

bt.insert(5, bt.root)
bt.insert(4, bt.root)
bt.insert(7, bt.root)
bt.insert(2, bt.root)
bt.insert(8, bt.root)
bt.insert(6, bt.root)
bt.insert(3, bt.root)
bt.insert(9, bt.root)

bt.print(bt.root)
bt.triangulos()

print(bt.triangulos())
