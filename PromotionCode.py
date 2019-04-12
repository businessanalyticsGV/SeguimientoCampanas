import pandas as pd
import numpy as np

Base_busqueda = pd.read_csv('E:\Procesos Sense\DB Blast\ListaPC_Busqueda.csv')
##print(Base_busqueda)

Catalogo_Codigos=pd.read_excel('E:\Procesos Sense\DB Blast\Catalogo Blast.xlsx')

Base_busqueda['Marca'] = [str([code for code in Catalogo_Codigos['PromotionCode'] if code in prom]) for prom in Base_busqueda['PromotionCode']]
Base_busqueda['Marca'] = [prom.replace('[',"") for prom in Base_busqueda['Marca']]
Base_busqueda['Marca'] = [prom.replace(']',"") for prom in Base_busqueda['Marca']]
Base_busqueda['Marca'] = [prom.replace("'","") for prom in Base_busqueda['Marca']]

Base_busqueda.rename(columns = {'PromotionCode':'PromotionCodeOrig','Marca':'PromotionCode'}, inplace = True)
Base_busqueda = Base_busqueda.merge(Catalogo_Codigos[['PromotionCode','Codigo','fecha de envio blast','Reusado']], how = 'left', on = ['PromotionCode'])

#Base_busqueda['Codigo']=np.where(Base_busqueda['DateCreated']>=Base_busqueda['fecha de envio blast'])
Base_busqueda.to_excel('E:\Procesos Sense\DB Blast\Base_PromotionCode_Trabajo.xlsx')

Base_busqueda.to_csv('Base_Prueba.csv')
