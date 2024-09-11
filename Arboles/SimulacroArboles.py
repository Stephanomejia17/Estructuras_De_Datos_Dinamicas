from arboles import GeneralTree
from BinaryTree import BinaryTree
"""E1. Dado un árbol general y un valor V, agregue un nuevo nodo con el valor 
V al nodo con más hijos del árbol."""

"""arbol = GeneralTree()

arbol.add_child(parent=None, child='A')
arbol.add_child(parent='A', child='B')
arbol.add_child(parent='A', child='C')
arbol.add_child(parent='A', child='D')
arbol.add_child(parent='B', child='E')
arbol.add_child(parent='B', child='F')
arbol.add_child(parent='B', child='G')
arbol.add_child(parent='E', child='K')
arbol.add_child(parent='E', child='L')
arbol.add_child(parent='E', child='M')
arbol.add_child(parent='F', child='N')
arbol.add_child(parent='G', child='O')
arbol.add_child(parent='C', child='H')
arbol.add_child(parent='C', child='I')
arbol.add_child(parent='D', child='J')
arbol.add_child(parent='J', child='P')
arbol.add_child(parent='J', child='Q')
arbol.add_child(parent='J', child='R')
arbol.add_child(parent='J', child='S')
arbol.add_child(parent='J', child='T')
arbol.add_child(parent='J', child='A')

#0.8 
def buscar_nodo_con_mas_hijos(node, value , tree, max_hijos = 0, value_node = ''):
                
    if len(node.children) == 0:
        return max_hijos, value_node
    
    else:
        max_hijos = len(node.children)
        for i in range(0, len(node.children)):
            value_node = node.value
            aux_max, value_node = buscar_nodo_con_mas_hijos(node.children[i], value, tree, max_hijos=max_hijos, value_node=value_node)
            if max_hijos <= aux_max:
                max_hijos = aux_max
    
    if node == tree.root:
        tree.add_child(value_node, value)
            
    
    return aux_max, value_node
        
arbol.print_tree()
a, b = buscar_nodo_con_mas_hijos(arbol.root, 'U', arbol)
arbol.print_tree()"""

"""
E2. Dado un árbol binario, un string S y un nivel N, responda si juntando 
todos los valores de los nodos del nivel L se puede formar S.
Por ejemplo, dado el árbol, el string "GRAVE" y el nivel 1 o 3 debería 
devolver True. Por otro lado, si el nivel es cualquier otro para este árbol, 
debería devolver False.
"""
0.8
def busqueda_de_palabras_horizontal(palabra, level, node, res = '', aux_level = 0, rpta = False):
    
    if level == aux_level:
        res += node.value
    else:
        
        if node.left_child is not None:
            res, rpta = busqueda_de_palabras_horizontal(palabra, level, node=node.left_child, res=res, aux_level=aux_level+1)
        if node.right_child is not None:
            res, rpta = busqueda_de_palabras_horizontal(palabra, level, node=node.right_child, res=res, aux_level=aux_level+1)
        
    
    if aux_level == 0 and palabra == res:
        rpta = True
        return res, rpta 

    return res, rpta
            
def busqueda_de_palabras_vertical(palabra, node, res = [], rpta = False, aux_res = '', switch = False):
    aux_res = ''
    
    for i in range(0, len(res)):
        aux_res += res[i] 
    
    if node.left_child is None and node.right_child is None:
        aux_res = ''
        res.append(node.value)
        for i in range(0, len(res)):
            aux_res += res[i] 
        if palabra == aux_res:
            switch = True
            return res,rpta,aux_res, switch
        
        return res, rpta, aux_res, switch
    else:
        res.append(node.value)
        if node.left_child is not None:
            res, rpta, aux_res, switch = busqueda_de_palabras_vertical(palabra, node.left_child, res=res, aux_res=aux_res)
            if switch == True:
                return res,rpta, aux_res, switch 
            elif palabra == aux_res and node.left_child is None and node.right_child is None:
                rpta = True
                return res, rpta, aux_res, switch
            res = res[:-1]
        if node.right_child is not None:
            res, rpta, aux_res, switch = busqueda_de_palabras_vertical(palabra, node.right_child, res=res, aux_res=aux_res)
            if switch == True:
                return res,rpta, aux_res, switch
            elif palabra == aux_res and node.left_child is None and node.right_child is None:
                rpta = True
                return res, rpta, aux_res, switch
            res = res[:-1]
    return res, rpta, aux_res, switch
        
bin_palabras = BinaryTree()
bin_palabras.insert('A', 'GRA', bin_palabras.root)
bin_palabras.insert('A', 'VE', bin_palabras.root)
bin_palabras.insert('GRA', 'S', bin_palabras.root)
bin_palabras.insert('GRA', 'Z', bin_palabras.root)
bin_palabras.insert('VE', 'X', bin_palabras.root)
bin_palabras.insert('VE', 'RR', bin_palabras.root)
bin_palabras.insert('S', 'G', bin_palabras.root)
bin_palabras.insert('S', 'R', bin_palabras.root)
bin_palabras.insert('G', 'D', bin_palabras.root)
bin_palabras.insert('G', 'Y', bin_palabras.root)
bin_palabras.insert('Z', 'A', bin_palabras.root)
bin_palabras.insert('X', 'V', bin_palabras.root)
bin_palabras.insert('RR', 'E', bin_palabras.root)
bin_palabras.insert('Y', 'XX', bin_palabras.root)
bin_palabras.print(bin_palabras.root)

print(busqueda_de_palabras_horizontal('GRAVE', 3, bin_palabras.root))
print(busqueda_de_palabras_vertical('AGRASGYXX', bin_palabras.root)[3])





"""E3. Dado un árbol binario de búsqueda, elimine TODOS los nodos cuyos 
valores sean mayores a un valor V siempre y cuando sean hojas huérfanas. 
Una hoja huérfana es un nodo hoja que es hijo único.
Por ejemplo, dado el siguiente árbol y un valor V = 50, los nodos que se 
deberían eliminar serían los que están marcados con X.

Las que tienen la marca azul no se deberían eliminar (el 7 no es mayor 
que 50, el 36 tampoco y el 300 si bien es mayor, no es una hoja huérfana)"""

"""bin_tree = BinaryTree()
bin_tree.insert(10, 5, bin_tree.root)
bin_tree.insert(10, 30, bin_tree.root)
bin_tree.insert(5, 7, bin_tree.root)
bin_tree.insert(30, 50, bin_tree.root)
bin_tree.insert(50, 40, bin_tree.root)
bin_tree.insert(50, 500, bin_tree.root)
bin_tree.insert(40, 36, bin_tree.root)
bin_tree.insert(500, 300, bin_tree.root)
bin_tree.insert(500, 505, bin_tree.root)
bin_tree.insert(505, 600, bin_tree.root)
bin_tree.print(bin_tree.root)

0.8
def elim_numeros(node, value, huerfano = False, father = None, left_right = None):
    
    if huerfano and node.left_child is None and node.right_child is None:
        if node.value > value and left_right == 0:
            father.left_child = None
        elif node.value > value and left_right == 1:
            father.right_child = None
        return father


    else:
        father = node
        if node.left_child is None or node.right_child is None:
            huerfano = True
        else:
            huerfano = False
        for i in range(0, 2):
            if i == 0 and node.left_child is not None:
                father = elim_numeros(node.left_child, value, huerfano=huerfano, father = father, left_right=i)
            elif i == 1 and node.right_child is not None:
                father = elim_numeros(node.right_child, value, huerfano=huerfano, father = father, left_right=i)   
        return father     
        
                         
elim_numeros(bin_tree.root, 1)
        
    
bin_tree.print(bin_tree.root)"""


