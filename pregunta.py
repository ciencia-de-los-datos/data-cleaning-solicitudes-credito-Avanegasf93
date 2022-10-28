"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df = df[df.columns[1:]]
    df.drop_duplicates(inplace=True)
    #df.drop(['Unnamed: 0'], axis=1,inplace=True)
    df.dropna(inplace=True)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True)


    df['sexo'] = df.sexo.drop_duplicates()
    df['sexo'] = df.sexo.str.lower()
    df['sexo'] = df.sexo.str.strip()

    df['tipo_de_emprendimiento'] = df.tipo_de_emprendimiento.drop_duplicates()
    df['tipo_de_emprendimiento'] = df.tipo_de_emprendimiento.str.lower()
    df['tipo_de_emprendimiento'] = df.tipo_de_emprendimiento.str.strip()

    df['idea_negocio'] = df.idea_negocio.drop_duplicates()
    df['idea_negocio'] = df.idea_negocio.str.replace("_", " ", regex=True)
    df['idea_negocio'] = df.idea_negocio.str.replace("-", " ", regex=True)
    df['idea_negocio'] = df.idea_negocio.str.lower()
    df['idea_negocio'] = df.idea_negocio.str.strip()

    df['monto_del_credito'] = df.monto_del_credito.drop_duplicates()
    df['monto_del_credito'] = df.monto_del_credito.str.replace(" ", "", regex=True)
    df['monto_del_credito'] = df.monto_del_credito.str.replace(",", "", regex=True)
    df['monto_del_credito'] = df.monto_del_credito.str.replace("$", "", regex=True)
    df['monto_del_credito'] = df.monto_del_credito.str.replace(".00", "", regex=True)
    df['monto_del_credito'] = df.monto_del_credito.str.strip()

    df['barrio'] = df.barrio.drop_duplicates()
    df['barrio'] = df.barrio.str.replace("_", " ", regex=True)
    df['barrio'] = df.barrio.str.replace("-", " ", regex=True)
    df['barrio'] = df.barrio.str.lower()
    df['barrio'] = df.barrio.str.strip()

    df['línea_credito'] = df.línea_credito.drop_duplicates()
    df['línea_credito'] = df.línea_credito.str.replace("_", " ", regex=True)
    df['línea_credito'] = df.línea_credito.str.replace("-", " ", regex=True)
    df['línea_credito'] = df.línea_credito.str.replace('soli diaria','solidaria', regex=True)
    df['línea_credito'] = df.línea_credito.str.lower()
    df['línea_credito'] = df.línea_credito.str.strip()

    df['barrio'] = df['barrio'].astype(str)
    df['línea_credito'] = df['línea_credito'].astype(str)
    df['monto_del_credito'] = df['monto_del_credito'].astype(float)


    df.drop_duplicates(inplace = True)
    return df
