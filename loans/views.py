import os
import joblib
import pandas as pd
from django.conf import settings
from django.shortcuts import render
from .models import LoanPrediction
from .forms import LoanForm


MODEL_PATH = os.path.join(settings.BASE_DIR, "ml", "loan_model.pkl")
model = joblib.load(MODEL_PATH)


def predict_loan(request):
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            # Convert form data into a DataFrame
            input_data = pd.DataFrame([form.cleaned_data])  # single row DataFrame

            # Ensure numeric fields are the correct type
            input_data["ApplicantIncome"] = input_data["ApplicantIncome"].astype(float)
            input_data["CoapplicantIncome"] = input_data["CoapplicantIncome"].astype(float)
            input_data["LoanAmount"] = input_data["LoanAmount"].astype(float)
            input_data["Loan_Amount_Term"] = input_data["Loan_Amount_Term"].astype(float)
            input_data["Credit_History"] = input_data["Credit_History"].astype(float)

            # Predict
            pred = model.predict(input_data)[0]
            result = "Approved" if pred == 1 else "Rejected"

            # Save to DB
            LoanPrediction.objects.create(
                Gender=form.cleaned_data["Gender"],
                Married=form.cleaned_data["Married"],
                Dependents=form.cleaned_data["Dependents"],
                Education=form.cleaned_data["Education"],
                Self_Employed=form.cleaned_data["Self_Employed"],
                ApplicantIncome=form.cleaned_data["ApplicantIncome"],
                CoapplicantIncome=form.cleaned_data["CoapplicantIncome"],
                LoanAmount=form.cleaned_data["LoanAmount"],
                Loan_Amount_Term=form.cleaned_data["Loan_Amount_Term"],
                Credit_History=float(form.cleaned_data["Credit_History"]),
                Property_Area=form.cleaned_data["Property_Area"],
                Prediction=result
            )

            return render(request, "result.html", {"result": result})
    else:
        form = LoanForm()
    return render(request, "home.html", {"form": form})

def history(request):
    loans = LoanPrediction.objects.all().order_by("-Created_At")
    return render(request, "history.html", {"loans": loans})