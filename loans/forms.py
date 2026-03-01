from django import forms

class LoanForm(forms.Form):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female")
    ]

    YES_NO_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No")
    ]

    PROPERTY_CHOICES = [
        ("Urban", "Urban"),
        ("Semiurban", "Semiurban"),
        ("Rural", "Rural")
    ]

    EDUCATION_CHOICES = [
        ("Graduate", "Graduate"),
        ("Not Graduate", "Not Graduate")
    ]

    EMPLOYED_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No")
    ]

    # Form fields
    Gender = forms.ChoiceField(choices=GENDER_CHOICES)
    Married = forms.ChoiceField(choices=YES_NO_CHOICES)
    Dependents = forms.ChoiceField(choices=[("0","0"),("1","1"),("2","2"),("3+","3+")])
    Education = forms.ChoiceField(choices=EDUCATION_CHOICES)
    Self_Employed = forms.ChoiceField(choices=EMPLOYED_CHOICES)
    ApplicantIncome = forms.IntegerField(min_value=0, label="Applicant Income")
    CoapplicantIncome = forms.IntegerField(min_value=0, label="Coapplicant Income")
    LoanAmount = forms.IntegerField(min_value=0, label="Loan Amount")
    Loan_Amount_Term = forms.IntegerField(min_value=0, label="Loan Amount Term (Months)")
    Credit_History = forms.ChoiceField(choices=[("1.0","Yes"), ("0.0","No")], label="Credit History")
    Property_Area = forms.ChoiceField(choices=PROPERTY_CHOICES)