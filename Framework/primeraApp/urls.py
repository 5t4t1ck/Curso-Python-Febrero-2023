from django.urls import path
from . import views

app_name = "primeraApp"

urlpatterns = [
    path('', views.homepage, name="homepage")
]
