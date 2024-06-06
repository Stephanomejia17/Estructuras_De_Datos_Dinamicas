class Grafo:
    def __init__(self) -> None:
        self.matriz_adyacencia = []
        self.size = 0
        self.values = []
        self.labels = []
    
    def add_vertex(self, value):
        self.values.append(value)
        if len(self.matriz_adyacencia) == 0:
            self.matriz_adyacencia.append([0])
            return
        else:
            for i in range(0, len(self.matriz_adyacencia)):
                self.matriz_adyacencia[i].append(0)
            lista_aux = []
            for i in range(len(self.values)):
                lista_aux.append(0)
            self.matriz_adyacencia.append(lista_aux)  
            
    def add_vertex_2(self, value):
        if value in self.labels:
            return "Etiqueta repetida"
        self.labels.append(value)
        for row in self.matriz_adyacencia:
            row.append(0)
        new_row = [0] * (self.size + 1)
        self.matriz_adyacencia.append(new_row)    
        self.size += 1   
        
        return "Nodo agregado"    
    
    def add_edge(self, v1, v2, bb1: bool):
        if v1 in self.values and v2 in self.values:
            idx1 = self.values.index(v1)
            idx2 = self.values.index(v2)    
        
        if idx1 is None:
            self.add_vertex(v1)
        elif idx2 is None:
            self.add_vertex(v2)
        else:
            if bb1 is True:
                self.matriz_adyacencia[idx1][idx2] = 1
                self.matriz_adyacencia[idx2][idx1] = 1
            else:
                self.matriz_adyacencia[idx1][idx2] = 1
                
    def add_edge_2(self, vertex_1, vertex_2, directed = True):
        if vertex_1 not in self.labels:
            self.add_vertex_2(vertex_1)
        if vertex_2 not in self.labels:
            self.add_vertex_2(vertex_2)
        
        v1_idx = self.labels.index(vertex_1)
        v2_idx = self.labels.index(vertex_2)
        
        self.matriz_adyacencia[v1_idx][v2_idx] = 1
        if not directed:
            self.matriz_adyacencia[v2_idx][v1_idx] = 1
            
    
    """def DFS(self, label, index_i = 0, index_j = 0, visitados = []):
        if label not in visitados:
            visitados.append(label)
            return self.DFS(label, index_i=index_i, index_j=index_j+1, visitados=visitados)
        
        else:
            for i in range(0, len(self.values)):
                if label == self.values[i]:
                    index_i=i
            for j in range(0, len(self.matriz_adyacencia)):
                label = self.values[j]
                if self.matriz_adyacencia[index_i][index_j] == 1 and label not in visitados:
                    visitados.append(label)
                    return self.DFS(label, index_i=j, index_j=0, visitados=visitados)"""
                    
    def DFS(self, label, index_i = 0, index_j = 0, visitados = []):
        if label not in visitados:
            visitados.append(label)
            index_i = self.values.index(label)
            return index_i
            

    def visualizar(self):
        for i in range(0, len(self.matriz_adyacencia)):
            print(self.matriz_adyacencia[i])
                
                
g1 = Grafo()


g1.add_vertex(5)
g1.add_vertex(4)
g1.add_vertex(3)
g1.add_vertex(2)

g1.add_edge(5,2, True)
g1.add_edge(3,4, True)
g1.add_edge(2,3, True)

print("Values: ", g1.values)
g1.visualizar()
print("DFS: ", g1.DFS(4))



