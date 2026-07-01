import joblib
import numpy as np
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
model_path = os.path.join(BASE_DIR, "model", "xgboost_model.joblib")

# Safe model loading with error handling
try:
    model = joblib.load(model_path)
    print(f"✅ Model loaded from: {model_path}")
except Exception as e:
    print(f"❌ Model load failed: {e}")
    model = None

FEATURE_ORDER = [
    "V1","V2","V3","V4","V5","V6","V7","V8","V9","V10",
    "V11","V12","V13","V14","V15","V16","V17","V18","V19","V20",
    "V21","V22","V23","V24","V25","V26","V27","V28","Amount"
]

def predict_fraud(data):
    if model is None:
        return {"error": "Model not loaded", "status": "ERROR"}
    
    try:
        input_data = np.array([[getattr(data, f) for f in FEATURE_ORDER]])
        prob = model.predict_proba(input_data)[0][1]
        pred = int(prob > 0.5)
        return {
            "prediction": pred,
            "probability": round(float(prob), 4),
            "status": "FRAUD" if pred == 1 else "LEGIT"
        }
    except Exception as e:
        return {"error": str(e), "status": "ERROR"}
