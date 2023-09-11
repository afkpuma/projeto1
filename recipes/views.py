from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
# As Views no Django são responsáveis por processar as requisições dos usuários, formar uma resposta e enviá-la de volta ao usuário.

def home(request):
    return render(request, 'recipes/home.html', context={
        'name':"yam alao",
    })

