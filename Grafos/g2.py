class Graph:
    def __init__(self) -> None:
        self.adj_list= {}
        self.size = 0
            
    def add_vertex(self, label):
        if label in self.adj_list.keys():
            return "Etiqueta repetida"
        
        self.adj_list[label] = []
        self.size += 1
        return "Etiqueta agregada"
    
                
    def add_edge(self, vertex_1, vertex_2, directed = True):
        if vertex_1 not in self.adj_list.keys():
            self.add_vertex(vertex_1)
        if vertex_2 not in self.adj_list.keys():
            self.add_vertex(vertex_2)
            
        self.adj_list[vertex_1].append(vertex_2)
        if not directed:
            self.adj_list[vertex_2].append(vertex_1)
            
    #0.1
    def grado_de_salida_mas_alto(self):
        mayor = 0
        nodo_mayor = None
        for keys in self.adj_list.keys():
            if len(self.adj_list[keys]) > mayor:
                mayor = len(self.adj_list.values())
                nodo_mayor = keys
        return nodo_mayor
    
    #0.2
    def grado_de_entrada_mas_alto(self):
        contadores = {key:0 for key in self.adj_list.keys()}
        
        for labels in self.adj_list.keys():
            
            for values in self.adj_list[labels]:
                if values in self.adj_list.keys():
                    contadores[values] += 1
                    

        return max(contadores.items(), key=lambda x: x[1])[0]   
    
    def DFS(self, vertex, visited=[]):
        if(vertex not in visited):
            visited.append(vertex)
            
            neighbors = self.adj_list[vertex]
            for n in neighbors:
                self.DFS(n, visited)
            return visited
    
    def BFS(self, start, visited=[], queue=[]):
        queue.append(start)
        while len(queue) > 0:
            first_value = queue[0]
            queue = queue[1:]
            if first_value not in visited:
                visited.append(first_value)
            for n in self.adj_list[first_value]:
                if n not in visited:
                    queue.append(n)
        
        return visited
            
    def ciclos(self, graph, visited=[], cont = 0):
        keys = list(graph.adj_list.keys())
        ciclos = []
        for n, i in enumerate(keys):
            visited = self.BFS(i)
            visited = visited[1:]
            if keys[n] in visited:
                cont += 1
                ciclos.append([i, keys[n]])
        
        if cont != 0:
            return True, cont, ciclos
        return False, cont, ciclos
                    
    def print_adj_list(self):
        print(self.adj_list)
                        

g1 = Graph()
g1.add_vertex("a")
g1.add_vertex("d")
g1.add_vertex("c")
g1.add_vertex("b")

g1.add_edge("a", "b")
g1.add_edge("d", "a")
g1.add_edge("a", "x")
g1.add_edge("c", "a")
g1.add_edge("c", "x")
g1.add_edge("c", "y")
g1.add_edge("x", "b")
g1.add_edge("y", "d")
g1.add_edge("x", "a")
g1.add_edge("y", "c")



g1.print_adj_list()


print(g1.BFS("c"))
print(g1.DFS("a"))
print(g1.ciclos(g1))