matriz = [[1,1,1,0], 
          [1,1,1,0], 
          [0,0,0,0], 
          [0,1,1,0]]


def grupos_de_grafos(matriz, aux_matriz = [], idx_aux = -1, cont = 0):
    for i in range(0, len(matriz)):  
        if 1 in matriz[i]:
            aux_matriz.append([])
            idx_aux += 1
            for j in range(0, len(matriz[i])):
                if (j == 0 and matriz[i][j] == 1) or ((matriz[i][j] == 1 and (matriz[i][j] == matriz[i][j-1] and matriz[i][j] == matriz[i-1][j])) or (j <= len(matriz[i]) and matriz[i][j] == matriz[i][j+1])):
                    aux_matriz[idx_aux].append(1)
                    cont += 1

            
    return cont, aux_matriz
    
            

print(grupos_de_grafos(matriz)  )  

