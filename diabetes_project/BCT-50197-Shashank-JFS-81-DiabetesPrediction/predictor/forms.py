from django import forms

class DiabetesForm(forms.Form):
    pregnancies = forms.FloatField(label='Pregnancies')
    glucose = forms.FloatField(label='Glucose')
    blood_pressure = forms.FloatField(label='Blood Pressure')
    skin_thickness = forms.FloatField(label='Skin Thickness')
    insulin = forms.FloatField(label='Insulin')
    bmi = forms.FloatField(label='BMI')
    diabetes_pedigree = forms.FloatField(label='Diabetes Pedigree Function')
    age = forms.FloatField(label='Age')
