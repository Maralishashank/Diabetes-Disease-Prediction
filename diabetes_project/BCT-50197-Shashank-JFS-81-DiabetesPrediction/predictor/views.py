from django.shortcuts import render
from .forms import DiabetesForm
from .models import Prediction
from .ml.predict import predict_single

def home(request):
    context = {}
    if request.method == 'POST':
        form = DiabetesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            features = [
                data['pregnancies'],
                data['glucose'],
                data['blood_pressure'],
                data['skin_thickness'],
                data['insulin'],
                data['bmi'],
                data['diabetes_pedigree'],
                data['age'],
            ]
            try:
                result, probability = predict_single(features)
            except Exception as e:
                context['error'] = (
                    "Model is not trained yet. Please run the training script. "
                    f"Details: {e}"
                )
                result = None
                probability = None

            if result is not None:
                Prediction.objects.create(
                    pregnancies=data['pregnancies'],
                    glucose=data['glucose'],
                    blood_pressure=data['blood_pressure'],
                    skin_thickness=data['skin_thickness'],
                    insulin=data['insulin'],
                    bmi=data['bmi'],
                    diabetes_pedigree=data['diabetes_pedigree'],
                    age=data['age'],
                    result=result,
                )

                context['result'] = result
                context['probability'] = f"{probability * 100:.2f}%"

        else:
            context['error'] = 'Please correct the errors below.'
    else:
        form = DiabetesForm()

    context['form'] = form
    return render(request, 'predictor/home.html', context)
