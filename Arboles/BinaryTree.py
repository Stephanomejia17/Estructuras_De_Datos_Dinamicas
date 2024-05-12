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
        
class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None
        self.altura = 0
    
    def insert(self, parent, children_value, node: Node):
        if self.root is None:
            self.root = Node(value=parent)
            self.root.setLeftChild(Node(value=children_value))
            self.altura += 1
            return True
        
        if node.value == parent:
            new_child = Node(children_value)
            if node.left_child is None:
                node.left_child = new_child
                return True
            elif node.right_child is None:
                node.right_child = new_child
                return True
            
        if node.left_child is not None:
            if self.insert(parent, children_value, node.left_child):
                return True
            
        if node.right_child is not None:
            if self.insert(parent, children_value, node.right_child):
                return True
        return False
    
    """def altura(self, node: Node):
        if self.root is None:
            return self.altura
        else:
            if node.left_child is not None:"""
            
    
    def print(self, node, prefix="", is_left=True):
        if not node:
            print("Empty Tree")
            return
        if node.right_child:
            self.print(node.right_child, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left_child:
            self.print(node.left_child, prefix + ("    " if is_left else "│   "), True)
            
bt = BinaryTree()

bt.insert(1, 2, bt.root)
bt.insert(1, 3, bt.root)
bt.insert(2, 4, bt.root)
bt.insert(2, 5, bt.root)
bt.insert(3, 6, bt.root)
bt.insert(3, 7, bt.root)
bt.insert(6, 3, bt.root)
bt.insert(3, 8, bt.root)
bt.insert(3, 8, bt.root)
bt.insert(8, 5, bt.root)
bt.insert(8, 6, bt.root)
bt.insert(8, 7, bt.root)
bt.insert(8, 8, bt.root)

print(bt.altura)

bt.print(bt.root)