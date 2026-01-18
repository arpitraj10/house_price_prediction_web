from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import HouseInput

import joblib
import numpy as np
from utils import confidence_interval

app = FastAPI(title="House Price Prediction Web")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model_data = joblib.load("model/house_price_model.pkl")
model = model_data["model"]
features = model_data["features"]

@app.get("/")
def health():
     return {"status": "House Price API Running"}

@app.post("/predict")
def predict_price(data: HouseInput):
    input_data = np.array([[
        data.overall_qual,
        data.gr_liv_area,
        data.garage_cars,
        data.total_bsmt_sf,
        data.year_built
    ]])

    prediction = model.predict(input_data)[0]
    std = np.std([tree.predict(input_data)[0] for tree in model.estimators_])

    return {
        "predicted_price": round(prediction, 2),
        "confidence_range": confidence_interval(prediction, std),
        "feature_importance": dict(zip(features, model.feature_importances_.tolist()))
    }





