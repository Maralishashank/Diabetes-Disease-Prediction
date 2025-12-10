# Diabetes Disease Prediction Using Machine Learning  
**Student Name:** M. Shashank  
**Register No.:** BCT-50197  
**Batch:** JFS – 81  

## 1. Abstract
Diabetes is one of the most common lifestyle diseases and early prediction helps in preventing serious complications. 
In this project, a web-based application is developed to predict whether a person is likely to have diabetes based on 
medical parameters such as glucose level, BMI and age. The system uses multiple machine learning algorithms and 
selects the best performing model for final prediction. The application is built using Java Full Stack concepts with 
a Python/Django based backend for the ML component, and can be easily deployed as a mini-project.

## 2. Introduction
The main aim of this project is to design and develop a user-friendly web application that predicts the presence of 
diabetes using historical medical data. Machine learning provides an automated way to learn patterns from data and 
make predictions for new patients. This project demonstrates how ML models can be integrated into a full-stack web 
application for a real-world healthcare use case.

## 3. Objectives
- To study the Pima Indians Diabetes dataset and understand the input features.  
- To train and compare different classification algorithms.  
- To select the best model based on accuracy and cross-validation scores.  
- To develop a web interface for entering patient details and displaying predictions.  
- To store prediction history in a database for future analysis.

## 4. System Requirements
**Software:**  
- Python 3.x, Django Framework  
- scikit-learn, pandas, numpy  
- SQLite / MySQL database  
- Any modern browser (Chrome, Edge, Firefox)  

**Hardware:**  
- Intel i3/i5 or above  
- Minimum 4 GB RAM  
- Stable internet connection (for installing dependencies)

## 5. Methodology
1. **Data Collection:** Pima Indians Diabetes dataset is used.  
2. **Pre-processing:** Dataset is loaded, and features and labels are separated.  
3. **Model Training:** Five algorithms are trained – K-Nearest Neighbour (KNN), Naïve Bayes, Decision Tree, 
   Random Forest and Support Vector Machine (SVM).  
4. **Model Selection:** The accuracy on the test set and cross-validation scores are compared and the best model is chosen.  
5. **Model Saving:** The best model is stored in a file (`best_model.pkl`) using joblib.  
6. **Web Integration:** A Django view loads the model, accepts form input and displays the prediction result on the UI.

## 6. Modules Description
- **User Interface Module:** HTML templates and CSS for collecting input from the user and showing the result.  
- **Prediction Module:** Python ML code to load the trained model and generate predictions.  
- **Persistence Module:** Django model (`Prediction`) to store prediction history in the database.  
- **Admin Module:** Django admin panel for viewing past predictions.

## 7. Implementation
The project follows an MVC-like structure using Django. The form is defined in `forms.py`, the database model in 
`models.py` and the business logic in `views.py`. The ML code is placed in the `ml` package. When the user submits 
the form, the view passes the input features to the `predict_single` function, and the output is displayed in a 
user-friendly message indicating high or low risk of diabetes.

## 8. Results and Discussion
The application successfully predicts the probability of diabetes based on the entered parameters. It provides a 
simple way for users to understand their risk level. Among the tested algorithms, the selected best model gives the 
highest accuracy on the test dataset. The project proves that integrating ML with web technologies is feasible and 
useful for healthcare decision support systems.

## 9. Conclusion
The Diabetes Disease Prediction project demonstrates the complete life cycle of a data science application – from 
data analysis and model training to deployment in a web environment. This mini-project is useful for learning both 
machine learning and full-stack development concepts and can be further enhanced by adding more features like 
authentication, charts and detailed analytics.

## 10. Future Enhancement
- Adding more clinical features and a larger dataset.  
- Deploying the application on cloud platforms.  
- Implementing role-based access for doctors and patients.  
- Visualizing prediction statistics using graphs and dashboards.

## 11. References
1. Kaggle – Pima Indians Diabetes Database.  
2. scikit-learn documentation.  
3. Django official documentation.
