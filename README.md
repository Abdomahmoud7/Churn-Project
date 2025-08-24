# 🌀 Customer Churn Detection API

This is an **End-to-End Machine Learning project** that predicts **customer churn** using historical customer data from a bank. The project is structured to cover the full ML lifecycle — from preprocessing and model training, to deployment using **FastAPI** as a RESTful web service.

---

## 📌 Project Structure

```
.
├── main.py                    ← FastAPI app with secured endpoints
├── config.py                  ← Loads models and environment variables
├── inference.py              ← Handles predictions logic
├── CustomerData.py           ← Input validation model using Pydantic
├── requirements.txt          ← Python dependencies
├── .env / .env.example       ← Environment variables (API key, version, etc.)
├── Churn_Modelling.csv       ← Raw dataset used for training
├── forest_tuned_model.pkl    ← Trained Random Forest model
├── xgb_tuned_model.pkl       ← Trained XGBoost model
├── preprocessor.pkl          ← Data preprocessing pipeline
├── notebook.ipynb            ← Data analysis & model training notebook
└── ...
```

---

## 🚀 Features

- 📊 Data preprocessing using pipelines (scaling, encoding, etc.)
- 🤖 Two trained ML models: `Random Forest` and `XGBoost`
- 🔐 Protected API endpoints using `X-API-Key`
- ⚙️ Modular and production-ready codebase
- 📦 Ready for deployment using `Uvicorn` + `FastAPI`

---

## 🧠 Tech Stack

| Layer         | Tools Used                                 |
|---------------|---------------------------------------------|
| Backend API   | FastAPI, Pydantic, Uvicorn                 |
| ML Models     | Scikit-learn, XGBoost                      |
| Data Pipeline | Scikit-learn Preprocessor + joblib         |
| Auth          | API Key via FastAPI Header Middleware      |
| Environment   | Python dotenv (.env) support               |

---

## 🧪 API Endpoints

> All endpoints are protected with an `X-API-Key` header.

| Method | Endpoint              | Description                                |
|--------|-----------------------|--------------------------------------------|
| `GET`  | `/`                   | Root endpoint (welcome message)            |
| `POST` | `/predict/forest`     | Predict churn using Random Forest model    |
| `POST` | `/predict/xgboost`    | Predict churn using XGBoost model          |

### 🔐 Header Required:
```http
X-API-Key: your_api_key_here
```

### 📥 Sample Request Body
```json
{
  "CreditScore": 650,
  "Geography": "France",
  "Gender": "Male",
  "Age": 35,
  "Tenure": 5,
  "Balance": 12500.75,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 0,
  "EstimatedSalary": 55000.0
}
```

---

## 🧾 Prediction Output

```json
{
  "churn_prediction": true,
  "churn_probability": 0.8421
}
```

---

## 🛠️ How to Run the Project

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Set environment variables**
> You can use `.env` or `.env.example`
```
APP_NAME=Churn-Detection
VERSION=1.0
SECRET_KEY_TOKEN=your_secret_key
```

3. **Run the server**
```bash
uvicorn main:app --reload
```

4. **Access Swagger UI**
```
http://127.0.0.1:8000/docs
```

---

## 📊 Model Training & Notebook

- All EDA, preprocessing, tuning, and model evaluation are provided in `notebook.ipynb` or `t.ipynb`.
- The models were serialized using `joblib` after hyperparameter tuning.

---

## 🔐 Security Note

- All API endpoints are protected with an API key (`X-API-Key`) to prevent unauthorized access.

---

## 📄 License

This project is for educational and demonstration purposes.  
You are free to modify and use it in your own work.

---

## ✨ Credits

Created by **Abdeltawab Mahmoud Ali**