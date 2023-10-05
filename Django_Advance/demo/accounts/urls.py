from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('login/', views.userLogin, name='home'),
    path('register/', views.userRegistration, name="register"),
    path('logout/', views.userLogout, name="logout"),
]