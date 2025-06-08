# app.py (Streamlit)
import streamlit as st
import requests

st.title("💼 Prédiction de Revenu Annuel")

# Choix du modèle
model_choice = st.selectbox("Choisissez un modèle de régression :", [
    "LinearRegression",
    "GradientBoostingRegressor",
    "MLPRegressor"
])

# Formulaire utilisateur
age = st.slider("🌐 Âge", 18, 70, 30)
categorie_age = st.selectbox("Catégorie d'âge", ["Jeune", "Adulte", "Sénior", "Âgé"])
sexe = st.selectbox("Sexe", ["Homme", "Femme"])
milieu = st.selectbox("Milieu", ["Urbain", "Rural"])
niveau_education = st.selectbox("Niveau d'éducation", ["Sans niveau", "Fondamental", "Secondaire", "Supérieur"])
experience = st.slider("Années d'expérience", 0, 50, 5)
etat_matrimonial = st.selectbox("État matrimonial", ["Célibataire", "Marié", "Divorcé", "Veuf"])
possede_voiture = st.selectbox("Possède une voiture ?", [0, 1])
possede_logement = st.selectbox("Possède un logement ?", [0, 1])
possede_terrain = st.selectbox("Possède un terrain ?", [0, 1])
socio_pro_group = st.selectbox("Groupe socioprofessionnel", [1, 2, 3, 4, 5, 6])
nombre_enfants = st.slider("Nombre d'enfants", 0, 10, 2)
charge_parentale = st.selectbox("Charge parentale ?", [0, 1])
travail_secondaire = st.selectbox("Travail secondaire ?", [0, 1])

if st.button("Prédire le revenu"):
    input_data = {
        "age": age,
        "categorie_age": categorie_age,
        "sexe": sexe,
        "milieu": milieu,
        "niveau_education": niveau_education,
        "experience": experience,
        "etat_matrimonial": etat_matrimonial,
        "possede_voiture": possede_voiture,
        "possede_logement": possede_logement,
        "possede_terrain": possede_terrain,
        "socio_pro_group": socio_pro_group,
        "nombre_enfants": nombre_enfants,
        "charge_parentale": charge_parentale,
        "travail_secondaire": travail_secondaire
    }

    response = requests.post(
        url=f"http://localhost:8000/predict?model={model_choice.lower()}",
        json=input_data
    )

    if response.status_code == 200:
        revenu = response.json()["revenu_annuel_prevu"]
        st.success(f"🌟 Revenu annuel prédit : {revenu:,.2f} DH")
    else:
        st.error("Une erreur est survenue : " + response.text)
