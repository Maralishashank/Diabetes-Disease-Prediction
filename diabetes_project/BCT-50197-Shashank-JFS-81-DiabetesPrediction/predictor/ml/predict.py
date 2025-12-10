from pathlib import Path
import numpy as np
import joblib

MODEL_PATH = Path(__file__).resolve().parent / 'best_model.pkl'

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found at {MODEL_PATH}. Run train_models.py first."
        )
    return joblib.load(MODEL_PATH)

def predict_single(input_list):
    """input_list: [pregnancies, glucose, blood_pressure, skin_thickness,
    insulin, bmi, diabetes_pedigree, age]"""
    model = load_model()
    arr = np.array(input_list).reshape(1, -1)
    prediction = model.predict(arr)[0]
    prob = getattr(model, "predict_proba", lambda x: [[0.0, 0.0]])(arr)[0]
    return int(prediction), float(prob[1])
