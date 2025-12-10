# 🌡️ Diabetes Disease Prediction – Machine Learning + Web App

> A smart health-tech mini-project that predicts diabetes risk using machine learning models and provides a clean user interface for testing predictions.

---

## 🚀 Project Overview

This full-stack application lets users enter medical parameters and instantly receive a **diabetes risk prediction** along with confidence percentage.

✔ ML algorithm comparison  
✔ Best model auto-selected  
✔ Simple UI for input + results  
✔ Stores history in database  

---

## ✨ Features

- Predict diabetes using clinical input
- Uses multiple ML models:
  - KNN  
  - Naive Bayes  
  - Decision Tree  
  - Random Forest  
  - SVM
- Model confidence score
- Django admin history view
- Clean frontend styling

---

## 🛠 Tech Stack

### Backend
- Python
- Django Framework
- SQLite (default) / MySQL supported

### Machine Learning
- scikit-learn  
- pandas  
- numpy  
- joblib

### Frontend
- HTML  
- CSS  

---

## 📂 Project Structure
📦 Diabetes Disease Prediction
 ┣ 📁 diabetes_site/          → Django project settings & configuration
 ┣ 📁 predictor/              → Main app
 │  ┣ 📁 ml/                  → Model training + prediction files
 │  ┣ 📁 templates/predictor/ → HTML pages
 │  ┣ 📁 static/predictor/    → CSS styles
 │  ┣ forms.py                → Input form fields
 │  ┣ models.py               → Database table for predictions
 │  ┣ views.py                → Handles form + ML prediction logic
 │  ┣ urls.py                 → Routing for app
 ┣ 📁 docs/                   → Mini project report + screenshots folder
 ┣ 📁 data/                   → Dataset folder (place diabetes.csv here)
 ┣ manage.py                  → Django management script
 ┣ requirements.txt           → Dependencies file
 ┗ README.md                  → Project documentation


