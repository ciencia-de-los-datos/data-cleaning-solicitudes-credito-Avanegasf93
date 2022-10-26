"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from dataclasses import replace


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df = df[df.columns[1:]]
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'])


    sexo_df = pd.DataFrame ({'sexo' : list(df.sexo)})
    sexo_df = sexo_df.drop_duplicates()
    df['sexo'] = df.sexo.str.lower()

    idea_negocio_df = pd.DataFrame ({'idea_negocio' : list(df.idea_negocio)})
    idea_negocio_df = idea_negocio_df.drop_duplicates()
    df['idea_negocio'] = df.idea_negocio.str.replace(" ", "_")
    df['idea_negocio'] = df.idea_negocio.str.replace("-", "_")
    df['idea_negocio'] = df.idea_negocio.str.lower()
    df['idea_negocio'] = df.idea_negocio.str.strip()

    estrato_df = pd.DataFrame ({'estrato' : list(df.estrato)})
    estrato_df = estrato_df.drop_duplicates()

    comuna_ciudadano_df = pd.DataFrame ({'comuna_ciudadano' : list(df.comuna_ciudadano)})
    comuna_ciudadano_df = comuna_ciudadano_df.drop_duplicates()

    monto_del_credito_df = pd.DataFrame ({'monto_del_credito' : list(df.monto_del_credito)})
    monto_del_credito_df = monto_del_credito_df.drop_duplicates()
    df['monto_del_credito'] = df.monto_del_credito.str.replace(" ", "")
    df['monto_del_credito'] = df.monto_del_credito.str.replace(",", "")
    df['monto_del_credito'] = df.monto_del_credito.str.replace("$", "")
    df['monto_del_credito'] = df.monto_del_credito.str.strip()

    línea_credito_df = pd.DataFrame ({'línea_credito' : list(df.línea_credito)})
    línea_credito_df = línea_credito_df.drop_duplicates()
    df['línea_credito'] = df.línea_credito.str.replace(" ", "_")
    df['línea_credito'] = df.línea_credito.str.replace("-", "_")
    df['línea_credito'] = df.línea_credito.str.lower()
    df['línea_credito'] = df.línea_credito.str.strip()

    df['barrio'] = df['barrio'].astype(str)
    df['línea_credito'] = df['línea_credito'].astype(str)
    df['monto_del_credito'] = df['monto_del_credito'].astype(float)


    df.drop_duplicates(inplace = True)

    return df
