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
        
            
        return contadores
    def print_adj_list(self):
        print(self.adj_list)
                
                
                

g1 = Graph()
g1.add_vertex("a")
g1.add_vertex("d")
g1.add_vertex("c")
g1.add_vertex("b")

g1.add_edge("a", "b")
g1.add_edge("c", "b")


g1.print_adj_list()
print(g1.grado_de_salida_mas_alto())
print(g1.grado_de_entrada_mas_alto())


"""g2 = {"a": 100, "b":10}

print(g2.items(), max(g2.items(), key=lambda x: x[1])[0])"""
