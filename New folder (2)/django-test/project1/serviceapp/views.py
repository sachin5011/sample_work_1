from django.shortcuts import render
from app1.models import appModel

def service(request):
    return(
        request,
        "test.html",
    )
