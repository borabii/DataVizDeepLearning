#!/bin/bash

# Vérifier si le répertoire de l'environnement virtuel existe
if [ ! -d "env" ]; then
    # Créer un nouvel environnement virtuel
    python -m venv env
fi
# Rendre le script exécutable
chmod +x run_app.sh

# Créer un nouvel environnement virtuel
python -m venv env

# Activer l'environnement virtuel
./env/Scripts/activate

# Installer les dépendances à partir du fichier requirements.txt
pip install -r ./requirements.txt

# Lancer l'application Streamlit
streamlit run ./src/main.py


