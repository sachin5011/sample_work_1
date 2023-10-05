from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'templates/index.html')

def userRegistration(request):
    return render(request, 'templates/register.html')

def userLogin(request):
    return HttpResponse('Login')

def userLogout(request):
    return HttpResponse('Logout')

# Create your views here.
