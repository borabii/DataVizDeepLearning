import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from visualization import df_conso_brute_viz,df_addresse_france_viz,viz_données_finale,geoloc_viz, visualization


def main():
    st.title("Projet Deep learning")

    # Sélecteur de section
    section = st.sidebar.selectbox("Sélectionnez une section :", [
                                   "Visualisation", "Prétraitement", "Visualisation après Prétraitement"])

    # Afficher la section sélectionnée
    if section == "Visualisation":
        visualisation()
    elif section == "Visualisation des predections":
        visualisation_predections()



def visualisation_données_brute():
    st.header("Section de Visualisation des données brutes")
    df_conso_brute_viz()
    df_addresse_france_viz()
    df_conso_brute_viz()


def visualisation():
    st.header("Section de Visualisation")
    viz_données_finale()
    geoloc_viz()
    visualization()
    

def visualisation_predections():
    st.header("Section de Visualisation des Prédictions")


if __name__ == "__main__":
    main()
