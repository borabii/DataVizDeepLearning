import pandas as pd



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

    return df_final_unique
