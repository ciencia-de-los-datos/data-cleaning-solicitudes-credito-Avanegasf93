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
    df.dropna(inplace=True)
    
    df["sexo"] = df["sexo"].apply(lambda x: str(x).lower().strip())

    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].apply(lambda x: str(x).lower().strip())

    df["idea_negocio"] = df["idea_negocio"].apply(lambda x: str(x).lower().strip())
    df["idea_negocio"] = df["idea_negocio"].apply(lambda x: str(x).replace("-"," ").replace("_"," ").strip())

    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x: str(x).lower().strip())
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x: str(x).strip("$").strip().replace(".00", "").replace(",", ""))

    df["barrio"] = df["barrio"].apply(lambda x: str(x).lower().replace("_"," ").replace("-"," "))
    df["línea_credito"] = df["línea_credito"].apply(lambda x: str(x).lower().strip())

    df["línea_credito"] = df["línea_credito"].apply(lambda x: str(x).lower().replace("-", " ").replace("_", " ").strip())

    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True)
    
    df.drop_duplicates(inplace=True)

    
    return df
