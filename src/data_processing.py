import pandas as pd
from get_data import read_conso_csv_file, read_adresse_csv_file


df_conso_brute = read_conso_csv_file()
# 
df_addresse_france_brute = read_adresse_csv_file()


def pretraitement(df_conso,df_adresse):
    #supprimer les colonnes 
    columns_to_keep = ['code_postal','latitude','longitude']
    df_adresse = df_adresse[columns_to_keep].copy()
    #supprimer les colonnes nulls dans longitude et latitude
    df_adresse.dropna(subset=['latitude', 'longitude'], inplace=True)
    
    #Renomer la colonne Code_postal
    df_conso = df_conso.rename(columns={'Code_postal': 'code_postal'})
    #Changer les types des colonnes
    df_conso['code_postal'] = df_conso['code_postal'].astype(str)
    df_adresse['code_postal'] = df_adresse['code_postal'].astype(str)
    df_conso['Année'] = df_conso['Année'].astype(str)
    # Merger df_conso avec df_adresse sur la colonne code postal
    df_final = pd.merge(df_conso, df_adresse, on='code_postal', how='left')
    #filter les données par années
    années_a_filtrer = ['2019','2020','2021']
    df_final_filtrer = df_final[df_final['Année'].isin(années_a_filtrer)]
    #Supprimer les lignes dupliquer 
    df_final_unique = df_final_filtrer.drop_duplicates(subset=['code_postal'])
    df_subset = df_final_unique.drop(columns=["Code Commune","code_postal","Code EPCI","Opérateur","Code Département","Filière","Libellé EPCI","Libellé Commune","Libellé Département","Libellé Région"])
   
   
    df_subset['Année'] = df_subset['Année'].astype(int)
    df_subset.dropna(subset=['latitude'], inplace=True)
    df_subset.dropna(subset=['longitude'], inplace=True)
    return df_subset

df_final = pretraitement(df_conso_brute,df_addresse_france_brute)

