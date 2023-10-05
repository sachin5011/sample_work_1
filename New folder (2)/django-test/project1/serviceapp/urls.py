from django.urls import path
from serviceapp.views import service

urlpatterns = [
    path('', service, name='service')
]