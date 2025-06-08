# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI()

# Dictionnaire des chemins de modèles
MODEL_PATHS = {
    "linearregression": "linearregression_model.joblib",
    "mlpregressor": "mlpregressor_model.joblib",
    "gradientboostingregressor": "gradientboostingregressor_model.joblib"
}

# Schéma d'entrée
class InputData(BaseModel):
    age: int
    categorie_age: str
    sexe: str
    milieu: str
    niveau_education: str
    experience: int
    etat_matrimonial: str
    possede_voiture: int
    possede_logement: int
    possede_terrain: int
    socio_pro_group: int
    nombre_enfants: int
    charge_parentale: int
    travail_secondaire: int

@app.post("/predict")
def predict(data: InputData, model: str):
    model_key = model.lower()
    if model_key not in MODEL_PATHS:
        raise HTTPException(status_code=404, detail="Modèle non trouvé")

    try:
        loaded_model = joblib.load(MODEL_PATHS[model_key])
    except:
        raise HTTPException(status_code=500, detail="Erreur de chargement du modèle")

    input_df = pd.DataFrame([data.dict()])
    prediction = loaded_model.predict(input_df)
    return {"revenu_annuel_prevu": round(float(prediction[0]), 2)}
