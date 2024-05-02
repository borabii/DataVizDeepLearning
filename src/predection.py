import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from get_data import read_conso_csv_file, read_adresse_csv_file
from data_processing import pretraitement
import folium
import streamlit as st


df_conso_brute = read_conso_csv_file()
#
df_addresse_france_brute = read_adresse_csv_file()

df_final = pretraitement(df_conso_brute, df_addresse_france_brute)


def train_and_evaluate_model(X_train_scaled, y_train, X_test_scaled, y_test):
    # Créer le modèle de réseau de neurones
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu',
                              input_shape=(X_train_scaled.shape[1],)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    # Compiler le modèle
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Entraîner le modèle
    model.fit(X_train_scaled, y_train, epochs=50,
              batch_size=32, validation_split=0.2, verbose=0)

    # Évaluer le modèle
    loss = model.evaluate(X_test_scaled, y_test)
    print("Perte (Loss) :", loss)

    return model


def make_predictions(model, X_test_scaled, y):
    # Obtenir les prédictions sur les données de test
    predictions = model.predict(X_test_scaled)
    # Comparer les prédictions avec les vraies valeurs de y dans les données de test
    results = []
    for i in range(len(predictions)):
        results.append(
            {"Valeur prédite": predictions[i][0], "Valeur réelle": y.values[i]})
    df_results = pd.DataFrame(results)
    return df_results


def get_prediction_results(df_subset):
    # Sélectionner les premières lignes du dataframe

    # Sélectionner toutes les colonnes sauf 'consommation_energie_finale'
    X = df_subset.drop(columns=["Consommation totale (MWh)"])
    y = df_subset["Consommation totale (MWh)"]

    # Fractionner les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.8, test_size=0.2, random_state=42)

    # Normaliser les données
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Entraîner et évaluer le modèle
    model = train_and_evaluate_model(
        X_train_scaled, y_train, X_test_scaled, y_test)

    # Faire des prédictions sur l'ensemble de données
    X_scaled = scaler.transform(X)  # Normaliser l'ensemble de données initial

    prediction_results = make_predictions(model, X_scaled, y)

    loss = model.evaluate(X_test_scaled, y_test)

    return prediction_results, loss


def pred_map(df):
    st.subheader(
        'Visualisation des prédections des consomations totals par commune')
    m = folium.Map(location=[48.8566, 2.3522], zoom_start=5)
    # Ajouter des marqueurs pour chaque station
    for index, row in df.iterrows():
        popup_text = f"Consommation_totale_predit: {row['Consommation_totale_predit']}"
        folium.Marker([row['latitude'], row['longitude']],
                      popup=popup_text).add_to(m)
    # Convertir la carte en HTML
    m_html = m.get_root().render()
    # Afficher la carte dans Streamlit
    st.components.v1.html(m_html, width=800, height=600)
    # Afficher la carte dans Streamlit en utilisant st.write pour afficher le HTML généré par Folium
