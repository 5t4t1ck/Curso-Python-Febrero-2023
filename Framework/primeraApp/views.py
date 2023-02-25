from django.shortcuts import render
from .models import Course

def homepage(request):
    return render(request, "primeraApp/inicio.html", {"courses":Course.objects.all})