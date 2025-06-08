# 💼 Projet IA - Prédiction du Revenu Annuel

Ce mini-projet d'intelligence artificielle a pour objectif de **prédire le revenu annuel des citoyens marocains** à partir de données socio-économiques simulées.

---

## 📓 Notebook

Le fichier `mini_projet_AI_LAMRANI_YOUSSEF_FAILALI_JATABI_HAYTHAM.ipynb` contient tout le processus de développement :

- Génération du dataset (`dataset_revenu_marocains.csv`) à partir de données simulées
- Nettoyage, transformation, normalisation
- Création des pipelines de préparation
- Entraînement des modèles de régression
- Sauvegarde des meilleurs modèles (`.joblib`)

## 📌 Fonctionnalités

- API de prédiction avec **FastAPI**
- Interface utilisateur simple et rapide avec **Streamlit**
- 3 modèles de régression disponibles :
  - `LinearRegression`
  - `GradientBoostingRegressor`
  - `MLPRegressor`
- Données simulées (dataset de 40 000 entrées)
- Analyse exploratoire via **Sweetviz**

---

## 🚀 Utilisation

### 1. Créer et activer un environnement virtuel

```bash
python -m venv env
.\env\Scripts\activate
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Lancer l'API FastAPI

```bash
uvicorn api:app --reload
```

Accès : [http://localhost:8000/docs](http://localhost:8000/docs)

![Streamlit interface](./img3.jpg)

### 4. Lancer l'application Streamlit

```bash
streamlit run app.py
```

---

## 🖼️ Interface utilisateur (exemple)

Voici quelques captures de l'application Streamlit :

### 🟦 Sélection du modèle et saisie des variables :

![Streamlit interface](./img1.jpg)

![Streamlit interface](./img2.jpg)
