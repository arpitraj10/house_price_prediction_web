import sys
import os
sys.path.append(os.getcwd())

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import HouseInput
import numpy as np
from fastapi import HTTPException
import os
import joblib

from backend.utils import load_model
from backend.predict import predict_price

app = FastAPI(title="House Price Prediction Web")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "model.pkl"


model = None

def get_model():
        global model
        if model is None:
                model = joblib.load("backend/model.pkl")
        return model        



@app.get("/")
def health():
     return {"status": "Backend running"}

@app.post("/predict")
def predict(data: HouseInput):
    model = get_model()
    prediction = model.predict([[...]])
    return {"price": prediction[0]}

    except Exception as e:
         print("ERROR:", e)
         raise HTTPException(status_code=500, detail=str(e))      










