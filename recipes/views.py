from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')