import pandas as pd
import numpy as np

Base_busqueda = pd.read_csv('E:\Procesos Sense\DB Blast\ListaPC_Busqueda.csv')
##print(Base_busqueda)

Catalogo_Codigos=pd.read_excel('E:\Procesos Sense\DB Blast\Catalogo Prueba Blast.xlsx')

Base_busqueda['Marca'] = [str([code for code in Catalogo_Codigos['PromotionCode'] if code in prom]) for prom in Base_busqueda['PromotionCode']]
Base_busqueda['Marca'] = [prom.replace('[',"") for prom in Base_busqueda['Marca']]
Base_busqueda['Marca'] = [prom.replace(']',"") for prom in Base_busqueda['Marca']]
Base_busqueda['Marca'] = [prom.replace("'","") for prom in Base_busqueda['Marca']]

Base_busqueda.to_excel('E:\Procesos Sense\DB Blast\Base_Prueba.xlsx')