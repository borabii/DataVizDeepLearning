from get_data import read_conso_csv_file, read_adresse_csv_file
from data_processing import pretraitement
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go   
import folium
df_conso_brute = read_conso_csv_file()
# 
df_addresse_france_brute = read_adresse_csv_file()


df_final = pretraitement(df_conso_brute,df_addresse_france_brute)

def df_conso_brute_viz():
    st.subheader('CSV Consomation électricité et gas')
    st.write(df_conso_brute.head(10))

def df_addresse_france_viz():
    st.subheader('CSV Communes De France')
    st.write(df_addresse_france_brute.head(10))

def viz_données_finale():
    st.subheader('Données brutes')
    st.dataframe(df_final.head(10))


def visualization_conso_par_filiere_operateur():
    st.subheader("Visualisation interactives")

    # Filtrer les colonnes numériques pour l'axe x
    colonnes_axe_x = ["Filière", "Opérateur"]
    axe_x = st.selectbox("Sélectionner une colonne pour l'axe x ", colonnes_axe_x)

    # Filtrer les colonnes non numériques pour l'axe y
    colonnes_axe_y = ["Consommation Agriculture (MWh)",
                      "Consommation Industrie (MWh)",
                      "Consommation Tertiaire  (MWh)",
                      "Consommation Résidentiel  (MWh)",
                      "Consommation Secteur Inconnu (MWh)",
                      "Consommation totale (MWh)"]
    axe_y = st.selectbox("Sélectionner une colonne pour l'axe y", colonnes_axe_y)
    data_for_chart = df_final[[axe_x, axe_y]].copy()

    # Conversion des données en valeurs numériques
    data_for_chart[axe_y] = pd.to_numeric(data_for_chart[axe_y], errors='coerce')

    # Supprimer les lignes avec des valeurs nulles
    data_for_chart = data_for_chart.dropna(subset=[axe_y])

    # Affichage du graphique à barres avec les données converties
    st.bar_chart(data_for_chart.set_index(axe_x))

def geoloc_viz():
    st.subheader('Carte des stations')
    df_cleaned = df_final.dropna(subset=['latitude', 'longitude'])
    # Créer une carte Folium
    m = folium.Map(location=[48.8566, 2.3522], zoom_start=5)

    # Ajouter des marqueurs pour chaque station
    for index, row in df_cleaned.iterrows():
        popup_text = f"Code postal: {row['code_postal']}, Consommation totale (MWh): {row['Consommation totale (MWh)']}"
        folium.Marker([row['latitude'], row['longitude']], popup=popup_text).add_to(m)

    # Afficher la carte dans Streamlit
     # Convertir la carte en HTML
    m_html = m.get_root().render()

    # Afficher la carte dans Streamlit
    st.components.v1.html(m_html, width=800, height=600)

    # Afficher la carte dans Streamlit en utilisant st.write pour afficher le HTML généré par Folium


def visualization_conso_total_par_année():
    st.subheader("Visualisation de la consomation total par année")
    fig = px.bar(df_final, x=df_final["Année"], y=df_final["Consommation totale (MWh)"])
    st.plotly_chart(fig)

    
