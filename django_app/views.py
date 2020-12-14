from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request, 'django_app/index.html', {'title': 'Home'})



def about(request):
    return render(request, 'django_app/about.html', {'title': 'About'})