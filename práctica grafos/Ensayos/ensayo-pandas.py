import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely import wkt

edges = pd.read_csv('c:/Users/steph/OneDrive/Documentos/Universidad de Medellin/Semestre III/Estructuras de Datos/práctica grafos/códigos_base/calles_de_medellin_con_acoso.csv', sep=';')

print(edges)

