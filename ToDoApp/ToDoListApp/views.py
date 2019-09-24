from django.shortcuts import render
from .models import People

def home(request):
    all_people = People.objects.all
    return render(request, "index.html", {'all_people':all_people})

def about(request):
    return render(request, "about.html")
