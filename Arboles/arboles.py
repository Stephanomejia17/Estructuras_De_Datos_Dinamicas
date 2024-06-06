class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.children: list = []

        
class GeneralTree:
    def __init__(self) -> None:
        self.root: Node = None
        self.Tam = 0

    
    def add_child(self, parent = None, child = None, aux_iter = None, switch = 0):
        if self.root is None:
            new_parent = Node(child)
            self.root = new_parent
            self.Tam += 1
            return True
        elif self.Tam >= 1 and switch == 0:
            aux_iter = self.root
        if aux_iter.value == parent:
            aux_iter.children.append(Node(child))
            self.Tam += 1
            return True
        if len(aux_iter.children) != 0:
            for i in range(0, len(aux_iter.children)):
                if self.add_child(parent=parent, child=child, aux_iter=aux_iter.children[i], switch=1):
                    return True
        return False
            
    def print_tree(self):
        if not self.root:
            print("Empty Tree")
            return

        def print_node(node, prefix="", is_last=True):
            print(prefix + ("└── " if is_last else "├── ") + str(node.value))
            if node.children:
                for i, child in enumerate(node.children):
                    print_node(child, prefix + ("    " if is_last else "│   "), i == len(node.children) - 1)
        
        print_node(self.root)

