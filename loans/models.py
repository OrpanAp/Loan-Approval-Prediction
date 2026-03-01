from django.db import models

# Create your models here.
class LoanPrediction(models.Model):
    GENDER_CHOICES = [("Male","Male"),("Female","Female")]
    YES_NO_CHOICES = [("Yes","Yes"),("No","No")]
    PROPERTY_CHOICES = [("Urban","Urban"),("Semiurban","Semiurban"),("Rural","Rural")]
    EDUCATION_CHOICES = [("Graduate","Graduate"),("Not Graduate","Not Graduate")]

    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    Married = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    Dependents = models.CharField(max_length=3)
    Education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    Self_Employed = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    ApplicantIncome = models.IntegerField()
    CoapplicantIncome = models.IntegerField()
    LoanAmount = models.IntegerField()
    Loan_Amount_Term = models.IntegerField()
    Credit_History = models.FloatField()
    Property_Area = models.CharField(max_length=10, choices=PROPERTY_CHOICES)
    Prediction = models.CharField(max_length=10)  # Approved/Rejected
    Created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Prediction} - {self.Created_At}"