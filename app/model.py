import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "model", "xgboost_model.joblib")

model = joblib.load(model_path)

FEATURE_ORDER = [
    "Time",
    "V1","V2","V3","V4","V5","V6","V7","V8","V9","V10",
    "V11","V12","V13","V14","V15","V16","V17","V18","V19","V20",
    "V21","V22","V23","V24","V25","V26","V27","V28","Amount"
]

def predict_fraud(data):
    input_data = np.array([[getattr(data, f) for f in FEATURE_ORDER]])

    prob = model.predict_proba(input_data)[0][1]   # fraud probability
    pred = int(prob > 0.5)

    return {
        "prediction": pred,
        "probability": float(prob),
        "status": "FRAUD" if pred == 1 else "LEGIT"
    }