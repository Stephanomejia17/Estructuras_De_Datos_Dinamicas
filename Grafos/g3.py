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
    
                
    def add_edge(self, vertex_1, vertex_2, peso,directed = True):
        if vertex_1 not in self.adj_list.keys():
            self.add_vertex(vertex_1)
        if vertex_2 not in self.adj_list.keys():
            self.add_vertex(vertex_2)
            
        self.adj_list[vertex_1].append((vertex_2, peso))
        if not directed:
            self.adj_list[vertex_2].append((vertex_1, peso))
    
    def ruta_mas_corta(self, Vertice1, Vertice2, aux_vertex=None,suma_ruta = 0, ruta = [], switch = 0, min_ruta = 99, min_list_ruta = [], rutas = []):
        if len(self.adj_list) == 0:
            return suma_ruta, ruta, rutas, min_ruta, min_list_ruta
        if switch == 0:
            aux_vertex = Vertice1
            switch = 1
        if aux_vertex == Vertice2:
            if min_ruta >= suma_ruta:
                min_ruta = suma_ruta
                min_list_ruta = ruta
            return suma_ruta, ruta, rutas, min_ruta, min_list_ruta
        else:
            
            for i in range(0, len(self.adj_list[aux_vertex])):
                if len(ruta) == 0 or ruta[0] != Vertice1:
                    ruta.append(Vertice1)
                ruta.append(self.adj_list[aux_vertex][i][0])
                suma_ruta += self.adj_list[aux_vertex][i][1]
                aux_vertex = self.adj_list[aux_vertex][i][0]
                if Vertice1 != ruta[-1]:
                    suma_ruta, ruta, rutas, min_ruta, min_list_ruta = self.ruta_mas_corta(Vertice1, Vertice2, aux_vertex, suma_ruta, ruta, switch=switch, min_ruta=min_ruta, min_list_ruta=min_list_ruta, rutas = rutas)

                aux_vertex = Vertice1
                if (ruta, suma_ruta) not in rutas:
                    rutas.append((ruta, suma_ruta))

                ruta = []
                suma_ruta = 0 
            for i in range(0, len(rutas)):
                if min_ruta >= rutas[i][1] and rutas[i][0] != [] and rutas[i][0][-1] == Vertice2:
                    min_ruta = rutas[i][1]
                    min_list_ruta = rutas[i][0]
            return suma_ruta, ruta, rutas, min_ruta, min_list_ruta          
                
      
    def ruta_mas_corta_2(self, Vertice1, Vertice2, aux_vertex=None,suma_ruta = 0, ruta = [], switch = 0, min_ruta = 99, min_list_ruta = [], rutas = []):
        aux_vertex = Vertice1
        for i in range(0, len(self.adj_list[aux_vertex])):
            if len(ruta) == 0:
                ruta.append(Vertice1)
            ruta.append(self.adj_list[aux_vertex][i][0]) 
            suma_ruta += self.adj_list[aux_vertex][i][1]
            if ruta[-1] == Vertice2:
                rutas.append((ruta, suma_ruta))
            ruta = []
            suma_ruta = 0
            
        for i in range(0, len(rutas)):
            if min_ruta >= rutas[i][1]:
                min_ruta = rutas[i][1]
                min_list_ruta = rutas[i][0]
        return min_ruta, min_list_ruta
    
    def print_graph(self):
        print("Grafo:")
        for vertex in self.adj_list:
            edges = self.adj_list[vertex]
            for edge in edges:
                print(f"{vertex} --({edge[1]})--> {edge[0]}")
            
    
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 5)
g.add_edge('C', 'B', 6)
g.add_edge('B', 'A', 7)
g.add_edge('B', 'B', 10)
g.print_graph()
a = g.ruta_mas_corta('A', 'B')
print(a[3], a[4])

m = Graph()
m.add_vertex("x")
m.add_vertex("y")
m.add_vertex("z")
m.add_vertex("a")
m.add_vertex("a")
m.add_edge("x", "y", 1) 
m.add_edge("x", "a", 4) 
m.add_edge("x", "c", 1) 
m.add_edge("b", "x", 10) 
m.add_edge("y", "z", 3) 
m.add_edge("z", "c", 5) 
m.add_edge("z", "x", 9) 
m.add_edge("c", "b", 2) 
m.print_graph()
b = (m.ruta_mas_corta('x', 'b'))
print(b[3], b[4])


