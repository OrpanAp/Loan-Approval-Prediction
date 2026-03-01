from django.contrib import admin
from .models import LoanPrediction

@admin.register(LoanPrediction)
class LoanPredictionAdmin(admin.ModelAdmin):
    list_display = ["id", "Prediction", "ApplicantIncome", "LoanAmount", "Created_At"]
    list_filter = ["Prediction", "Property_Area", "Credit_History"]
    search_fields = ["Gender", "Education"]