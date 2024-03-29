from get_data import read_conso_csv_file, read_adresse_csv_file
from data_processing import pretraitement
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go   

df_conso_brute = read_conso_csv_file()
# 
df_addresse_france_brute = read_adresse_csv_file()


df_final = pretraitement(df_conso_brute,df_addresse_france_brute)

def df_conso_brute_viz():
    st.subheader('CSV Consomation électricité et gas')
    st.write(df_conso_brute)

def df_addresse_france_viz():
    st.subheader('CSV Communes De France')
    st.write(df_conso_brute)

def viz_données_finale():
    st.subheader('Données brutes')
    st.write(df_final)


def visualization():
    st.subheader("Visualisation interactives")

    # Sélectionnez deux colonnes à afficher
    column1 = st.selectbox("Sélectionner la première colonne", df_final.columns)
    column2 = st.selectbox("Sélectionner la deuxième colonne", df_final.columns)

    # Visualisation en nuage de points
    fig = px.scatter(df_final, x=column1, y=column2)
    st.plotly_chart(fig)

def geoloc_viz():
    st.subheader('Carte des stations')
    
    fig = go.Figure(go.Scattermapbox(
        lat=df_final["latitude"], 
        lon=df_final["longitude"], 
        mode='markers',
        marker=dict(
            size=10,
            color='red', 
            opacity=0.8
        ),
        text="code_postal"+ df_final["code_postal"] + ": Consommation totale (MWh) " + df_final["Consommation totale (MWh)"].astype(str),  # Text to display on hover
        hoverinfo='text' 
    ))
    
    st.title("Répartition des zones de réseaux")
    fig.update_layout(
        mapbox_style="open-street-map", 
        autosize=True,
        margin=dict(l=0, r=0, t=0, b=0),
        mapbox=dict(center=go.layout.mapbox.Center(lat=48.8566, lon=2.3522), zoom=5)
    )
    
    st.plotly_chart(fig)

    
