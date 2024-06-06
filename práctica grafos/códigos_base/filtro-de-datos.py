import pandas as pd

file = pd.read_csv('c:/Users/steph/OneDrive/Documentos/Universidad de Medellin/Semestre III/Estructuras de Datos/práctica grafos/códigos_base/calles_de_medellin_con_acoso.csv', sep=';')


matriz = file.values.tolist()
print('name;length;oneway;harassmentRisk')
new_matriz = [[matriz[i][j] for j in range(0, len(matriz[i])) if j != 1 and j != 2 and j != 6] for i in range(0, len(matriz))]
for i in range(0, 10):
    print(new_matriz[i])