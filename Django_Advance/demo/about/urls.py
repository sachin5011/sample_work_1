from django.urls import path
from . import views

urlpatterns = [
    path('aboutuser/', views.aboutUser, name='aboutuiser'),
    path('aboutproduct/', views.aboutProduct, name="aboutproduct")
]