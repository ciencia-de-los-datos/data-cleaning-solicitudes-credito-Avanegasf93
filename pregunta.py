"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    
   df = pd.read_csv("solicitudes_credito.csv", sep=";")
   df.drop(['Unnamed: 0'], axis=1,inplace=True)

   df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)

   df.sexo = df.sexo.str.lower()
   df.sexo = df.sexo.strip()

   df.idea_negocio = df.idea_negocio.str.lower()
   df.idea_negocio = df.idea_negocio.str.strip('_')
   df.idea_negocio = df.idea_negocio.str.strip('-')
   df.idea_negocio = df.idea_negocio.str.strip()
   df.idea_negocio = df.idea_negocio.str.replace("_", "-")
   df.idea_negocio = df.idea_negocio.str.replace("-", " ")

   df.monto_del_credito = df.monto_del_credito.str.replace('$','')
   df.monto_del_credito = df.monto_del_credito.str.replace(',','')
   df.monto_del_credito = df.monto_del_credito.astype(float)

   df.barrio = df.barrio.str.lower()
   df.barrio = df.barrio.str.strip()
   df.barrio = df.barrio.str.replace("_", "-")
   df.barrio = df.barrio.str.replace("-", " ")

   df.línea_credito = df.línea_credito.str.lower()
   df.línea_credito = df.línea_credito.str.strip('_')
   df.línea_credito = df.línea_credito.str.strip('-')
   df.línea_credito = df.línea_credito.str.strip()
   df.línea_credito = df.línea_credito.str.replace("_", "-")
   df.línea_credito = df.línea_credito.str.replace("-", " ")

   df.dropna(inplace=True)
   df.drop_duplicates(inplace=True)


   return df
