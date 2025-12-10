"""Training script for Diabetes Prediction models.

This script expects a CSV file `data/diabetes.csv` with the Pima Indians Diabetes Dataset.
Columns commonly used:
    Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
    BMI,DiabetesPedigreeFunction,Age,Outcome
"""

import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_DIR / 'data' / 'diabetes.csv'
MODEL_DIR = Path(__file__).resolve().parent
MODEL_PATH = MODEL_DIR / 'best_model.pkl'

def load_data():
    df = pd.read_csv(DATA_PATH)
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    return X, y

def train_and_select_model():
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    models = {
        'KNN': KNeighborsClassifier(),
        'NaiveBayes': GaussianNB(),
        'DecisionTree': DecisionTreeClassifier(random_state=42),
        'RandomForest': RandomForestClassifier(random_state=42),
        'SVM': SVC(probability=True, random_state=42),
    }

    best_model = None
    best_accuracy = 0.0

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        print(f"{name} Test Accuracy: {acc:.4f}")

        cv_scores = cross_val_score(model, X, y, cv=5)
        print(f"{name} CV Accuracy: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

        if acc > best_accuracy:
            best_accuracy = acc
            best_model = model

    joblib.dump(best_model, MODEL_PATH)
    print(f"Best model saved with accuracy: {best_accuracy:.4f}")

if __name__ == '__main__':
    train_and_select_model()
