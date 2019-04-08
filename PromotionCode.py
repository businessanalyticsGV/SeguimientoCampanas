import pandas as pd
import numpy as np

df = pd.read_csv('E:/Procesos Sense/Catalogos/baseBOB.csv')
df = df[pd.notnull(df['PromotionCode'])]

df_cat = pd.read_excel('E:/Procesos Sense/Catalogos/CodigosICE.xlsx')

df['llave'] = [str([code for code in df_cat['Group Code'] if code in prom]) for prom in df['PromotionCode']]
df['llave'] = [prom.replace('[',"") for prom in df['llave']]
df['llave'] = [prom.replace(']',"") for prom in df['llave']]
df['llave'] = [prom.replace("'","") for prom in df['llave']]
df.to_excel('E:/Procesos Sense/Catalogos/CodigoICEGallery_Python.xlsx')



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