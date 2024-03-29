import pandas as pd



def pretraitement(df_conso,df_adresse):
    #supprimer les colonnes 
    columns_to_keep = ['code_postal','latitude','longitude',]
    df_adresse = df_adresse[columns_to_keep].copy()
    #supprimer les colonnes nulls dans longitude et latitude
    df_adresse.dropna(subset=['latitude', 'longitude'], inplace=True)
    #rajouter la colonne  dans df_conso 
  
    df_conso = df_conso.rename(columns={'Code_postal': 'code_postal'})
    df_conso['code_postal'] = df_conso['code_postal'].astype(str)
    df_adresse['code_postal'] = df_adresse['code_postal'].astype(str)
    # Merge df_conso with df_adresse on the code postal column
    df_final = pd.merge(df_conso, df_adresse, on='code_postal', how='left')
    df_unique = df_final.drop_duplicates(subset=['code_postal'])       

    
    
    return df_unique
    