from django.http import HttpResponse
from django.shortcuts import render

# accountapp/views.py

# Create your views here.

def hello_world(request):
    return render(request, 'base.html')