from django.urls import path
from . import views

urlpatterns = [
    path("", views.predict_loan, name="predict_loan"),
    path("history/", views.history, name="history"),
]