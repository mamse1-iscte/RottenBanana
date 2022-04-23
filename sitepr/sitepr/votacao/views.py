from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .models import Filme_ou_serie

def index(request):
    latest_question_list =Filme_ou_serie.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'criaConta', context)

def boas(request):
    return render(request, 'votacao/boas.html')

def fazerLogin(request):
    return render(request, 'votacao/fazerLogin.html')

def criaConta(request):
    return render(request, 'votacao/criaConta.html')


def HomePage(request):
    return render(request, 'votacao/HomePage.html')

def criarUserPage(request):
    return render(request, 'votacao/criarUser.html')




