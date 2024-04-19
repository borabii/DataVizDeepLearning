import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from visualization import df_conso_brute_viz,df_addresse_france_viz,viz_données_finale,geoloc_viz, visualization_conso_par_filiere_operateur,visualization_conso_total_par_année


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


if __name__ == "__main__":
    main()
