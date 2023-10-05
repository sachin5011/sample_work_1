from django.urls import path
from app1.views import home, testmodel

urlpatterns = [
    path('', home, name='home'),
    path('test/', testmodel, name="testmodel"),
]