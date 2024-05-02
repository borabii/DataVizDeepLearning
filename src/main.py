from predection import get_prediction_results, pred_map
import streamlit as st
import pandas as pd
from get_data import read_conso_csv_file, read_adresse_csv_file
import plotly.express as px
import plotly.graph_objects as go
from visualization import df_conso_brute_viz, df_addresse_france_viz, viz_données_finale, geoloc_viz, visualization_conso_par_filiere_operateur, visualization_conso_total_par_année
from data_processing import pretraitement


df_conso_brute = read_conso_csv_file()
#
df_addresse_france_brute = read_adresse_csv_file()

df_final = pretraitement(df_conso_brute, df_addresse_france_brute)


def main():
    st.title("Projet Deep learning")

    # Sélecteur de section
    section = st.sidebar.selectbox("Sélectionnez une section :", [
                                   "Visualisation des données brutes", "Visualisation après Prétraitement", "predections"])

    # Afficher la section sélectionnée
    if section == "Visualisation des données brutes":
        visualisation_données_brute()
    elif section == "Visualisation après Prétraitement":
        visualisation()
    elif section == "predections":
        visualisation_predections()


def visualisation_données_brute():
    st.header("Section de Visualisation des données brutes")
    df_conso_brute_viz()
    df_addresse_france_viz()


def visualisation():
    st.header("Section de Visualisation des données pré-traiter")
    viz_données_finale()
    geoloc_viz()
    visualization_conso_par_filiere_operateur()
    visualization_conso_total_par_année()


def visualisation_predections():
    st.header("Section de Visualisation des Prédictions")
    prediction_results, loss = get_prediction_results(df_final)

    # Afficher la perte (loss)
    st.subheader("Perte (Loss)")
    st.write("Perte (Loss) :", loss)

    # Afficher les résultats de prédiction
    st.write(prediction_results)
    print(prediction_results)
    st.header("Section de Visualisation des Prédictions")
    # Ajouter les prédictions à une nouvelle colonne dans le DataFrame
    df_avec_pred = df_final.drop(columns=["Consommation totale (MWh)"])
    # Sélectionne uniquement la première colonne
    nouvelle_colonne_df = prediction_results.iloc[:, 0]
    print(nouvelle_colonne_df)
    df_avec_pred['Consommation_totale_predit'] = nouvelle_colonne_df
    df_avec_pred.to_csv('./tt.csv')
    pred_map(df_avec_pred)


if __name__ == "__main__":
    main()
