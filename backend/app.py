from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import HouseInput
import numpy as np
from fastapi import HTTPException
import os
import joblib

from backend.utils import confidence_interval

app = FastAPI(title="House Price Prediction Web")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")


model = joblib.load(MODEL_PATH)


@app.get("/")
def health():
     return {"status": "API is running"}

@app.post("/predict")
def predict(data: HouseInput):
    try:
         features = np.array([[
              data.overall_qual,
              data.gr_liv_area,
              data.garage_cars,
              data.total_bsmt_sf,
              data.full_bath,
              data.year_built
         ]])

         prediction = model.predict(features)[0]

         return {
              "predicted_price": float(prediction)
         }

    except Exception as e:
         print("ERROR:", e)
         raise HTTPException(status_code=500, detail=str(e))      






