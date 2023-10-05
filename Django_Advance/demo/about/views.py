from django.shortcuts import render, HttpResponse

def aboutUser(request):
    return HttpResponse("About user page")

def aboutProduct(request):
    return HttpResponse('About Product Page')

# Create your views here.
