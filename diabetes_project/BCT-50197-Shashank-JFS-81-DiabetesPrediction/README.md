# Diabetes Disease Prediction Using Machine Learning

Full-stack web application for predicting the likelihood of diabetes using multiple
machine learning algorithms (KNN, Naïve Bayes, Decision Tree, Random Forest, SVM).

## Tech Stack

- Python
- Django (backend + templates)
- SQLite (default, easily switchable to MySQL via Django ORM)
- HTML, CSS (frontend)
- scikit-learn, pandas, numpy, joblib

## Project Structure

- `diabetes_site/` - Django project configuration
- `predictor/` - Main app with:
  - `forms.py` - Form for patient input
  - `models.py` - Prediction history model
  - `views.py` - Prediction logic and page rendering
  - `ml/` - Machine learning training and prediction modules
  - `templates/predictor/` - HTML templates
  - `static/predictor/` - CSS styles
- `manage.py` - Django management script

## Setup Instructions

1. Create and activate a virtual environment (recommended).
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download the Pima Indians Diabetes Dataset (CSV) from a trusted open-source source
   (for example, Kaggle) and place it at:

   ```text
   data/diabetes.csv
   ```

   Ensure it has the columns:

   ```text
   Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
   BMI,DiabetesPedigreeFunction,Age,Outcome
   ```

4. Train the models and save the best one:

   ```bash
   python predictor/ml/train_models.py
   ```

5. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your browser at `http://127.0.0.1:8000/` and use the form to get predictions.

## Using MySQL Instead of SQLite

- Install a MySQL server and a Python MySQL client (e.g., `mysqlclient`).
- Update the `DATABASES` section in `diabetes_site/settings.py` with your MySQL details.
- Run migrations again.

## Notes

- The best-performing model is saved to `predictor/ml/best_model.pkl`.
- The web UI is responsive and beginner-friendly, suitable for demos and GitHub portfolio.
- You can extend the project by adding charts for accuracy comparison, user authentication, etc.
