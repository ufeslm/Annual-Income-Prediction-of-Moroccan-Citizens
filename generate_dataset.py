import pandas as pd
import numpy as np
import random

# Fixer la seed pour la reproductibilité
np.random.seed(42)

# Nombre d’enregistrements
n = 40000

# Variables de base simulées
ages = np.random.randint(18, 70, size=n)
sexes = np.random.choice(["Homme", "Femme"], size=n, p=[0.55, 0.45])
milieux = np.random.choice(["Urbain", "Rural"], size=n, p=[0.65, 0.35])
education_levels = np.random.choice(["Sans niveau", "Fondamental", "Secondaire", "Supérieur"], size=n, p=[0.25, 0.35, 0.25, 0.15])
experience = np.clip(ages - np.random.randint(16, 25, size=n), 0, None)
etat_matrimonial = np.random.choice(["Célibataire", "Marié", "Divorcé", "Veuf"], size=n, p=[0.4, 0.45, 0.1, 0.05])
possession_voiture = np.random.choice([0, 1], size=n, p=[0.7, 0.3])
possession_logement = np.random.choice([0, 1], size=n, p=[0.6, 0.4])
possession_terrain = np.random.choice([0, 1], size=n, p=[0.85, 0.15])
socio_group = np.random.choice([1, 2, 3, 4, 5, 6], size=n, p=[0.05, 0.15, 0.2, 0.25, 0.2, 0.15])

# Variables ajoutées
nbr_enfants = np.random.poisson(2, size=n)
charge_parentale = np.random.choice([0, 1], size=n, p=[0.6, 0.4])
travail_secondaire = np.random.choice([0, 1], size=n, p=[0.85, 0.15])

# Catégorie d’âge
def categoriser_age(age):
    if age < 26:
        return "Jeune"
    elif age < 40:
        return "Adulte"
    elif age < 60:
        return "Sénior"
    else:
        return "Âgé"

categorie_age = np.array([categoriser_age(a) for a in ages])

# Génération du revenu avec bruit
base_revenu = (
    12000 +
    (ages * 100) +
    (experience * 150) +
    (np.where(sexes == "Homme", 2000, -1000)) +
    (np.where(milieux == "Urbain", 6000, -3000)) +
    (np.array([{"Sans niveau": 0, "Fondamental": 2000, "Secondaire": 5000, "Supérieur": 10000}[e] for e in education_levels])) +
    (np.array([8000 - g * 1000 for g in socio_group])) +
    (possession_voiture * 3000 + possession_logement * 5000 + possession_terrain * 2000)
)

revenus = base_revenu + np.random.normal(0, 3000, size=n)
revenus = np.clip(revenus, 2000, None)  # Minimum revenu

# Injecter valeurs manquantes (5% aléatoirement)
for col in ["education_levels", "etat_matrimonial", "revenus"]:
    mask = np.random.rand(n) < 0.05
    vars()[col][mask] = None

# Créer le DataFrame
df = pd.DataFrame({
    "age": ages,
    "categorie_age": categorie_age,
    "sexe": sexes,
    "milieu": milieux,
    "niveau_education": education_levels,
    "experience": experience,
    "etat_matrimonial": etat_matrimonial,
    "possede_voiture": possession_voiture,
    "possede_logement": possession_logement,
    "possede_terrain": possession_terrain,
    "socio_pro_group": socio_group,
    "revenu_annuel": revenus,
    "nombre_enfants": nbr_enfants,
    "charge_parentale": charge_parentale,
    "travail_secondaire": travail_secondaire,
    "colonne_redundante": ages,  # Redondante
    "non_pertinente": "N/A"  # Non pertinente
})

# Injecter quelques valeurs aberrantes
df.loc[df.sample(frac=0.005).index, "revenu_annuel"] *= 5

# Sauvegarder le CSV
csv_path = "dataset_revenu_marocains.csv"
df.to_csv(csv_path, index=False)
