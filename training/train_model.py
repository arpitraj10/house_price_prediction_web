import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
import os

# Load dataset
df = pd.read_csv("../dataset/cleaned_data.csv")
print(df.columns)
exit()

# Select ONLY numeric features used in API
features = [
    "overall_qual",
    "gr_liv_area",
    "garage_cars",
    "total_bsmt_sf",
    "yearbuilt"
]

target = "sale_price"

X = df[features]
y = df[target]

# Train model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

# Save model
os.makedirs("../backend/mode1", exist_ok=True)
joblib.dump(model, "../backend/model.pkl")

print("Model trained and saved successfully")
