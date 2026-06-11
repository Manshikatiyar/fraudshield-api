from fastapi import FastAPI
from app.schemas import TransactionInput
from app.model import predict_fraud

app = FastAPI(
    title="FraudShield API",
    description="Credit Card Fraud Detection using XGBoost",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def home():
    return {
        "message": "FraudShield API is running 🚀",
        "status": "healthy"
    }

# Prediction endpoint
@app.post("/predict")
def predict(data: TransactionInput):
    return predict_fraud(data)