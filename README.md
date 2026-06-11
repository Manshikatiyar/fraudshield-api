# 🛡️ FraudShield - Credit Card Fraud Detection API

An end-to-end Machine Learning project that detects fraudulent credit card transactions using an XGBoost model, deployed using FastAPI, Docker, and Render.

---

## 🚀 Live Demo

- 🌐 API: https://fraudshield-api-33e8.onrender.com
- 📘 Swagger UI: https://fraudshield-api-33e8.onrender.com/docs

---

## 🧠 Problem Statement

Detect fraudulent credit card transactions using historical transaction data and classify them as:

- ✅ Legit (0)
- 🚨 Fraud (1)

---

## ⚙️ Tech Stack

- Python
- FastAPI
- XGBoost
- Scikit-learn
- Pandas / NumPy
- Docker
- Render (Cloud Deployment)

---

## 📊 Machine Learning Model

- Algorithm: XGBoost Classifier
- Input Features:
  V1–V28 + Amount (+ Time if used)
- Output:
  - 0 → Legit Transaction
  - 1 → Fraudulent Transaction

---

## 📁 Project Structure

fraudshield-api/
│
├── app/
│   ├── main.py        # FastAPI entry point
│   ├── model.py       # ML model loading & prediction logic
│   ├── schemas.py     # Input validation using Pydantic
│
├── model/
│   └── xgboost_model.joblib   # Trained ML model
│
├── requirements.txt
├── Dockerfile
└── README.md

---

## 📡 API Endpoints

### 🏠 Home

GET /

Response:
```json
{"message": "FraudShield API is running 🚀"}
```

---

### 🔍 Predict Fraud

POST /predict

Request Body:
```json
{
  "V1": 0.1,
  "V2": -1.2,
  "V3": 2.3,
  "V4": 0.5,
  "V5": -1.0,
  "V6": 0.3,
  "V7": -0.2,
  "V8": 0.1,
  "V9": -1.1,
  "V10": 0.4,
  "V11": -0.5,
  "V12": 1.2,
  "V13": 0.6,
  "V14": -0.9,
  "V15": 0.2,
  "V16": -0.3,
  "V17": 0.8,
  "V18": -0.7,
  "V19": 0.5,
  "V20": -0.2,
  "V21": 0.1,
  "V22": -0.4,
  "V23": 0.3,
  "V24": 0.2,
  "V25": -0.1,
  "V26": 0.4,
  "V27": -0.3,
  "V28": 0.2,
  "Amount": 120.5
}
```

Response:
```json
{
  "prediction": 1,
  "probability": 0.91,
  "status": "FRAUD"
}
```

---

## 🐳 Run with Docker

```bash
docker build -t fraudshield-api .
docker run -p 8000:8000 fraudshield-api
```

---

## 💻 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## ☁️ Deployment (Render)

Steps:
1. Push code to GitHub
2. Connect repository to Render
3. Select Docker environment
4. Deploy automatically

---

## 🚀 Features

- Real-time fraud detection
- Probability scoring
- REST API
- Swagger UI testing
- Dockerized deployment
- Cloud hosting (Render)

---

## 🔮 Future Improvements

- JWT Authentication
- Database logging
- Frontend dashboard
- Model retraining pipeline (MLOps)
- Monitoring system

---

## 👨‍💻 Author

Built by **Manshi Katiyar**

---

## ⭐ Support

If you like this project, give it a star ⭐ on GitHub
