from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):

    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def user_login(request):

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')

        user_auth = authenticate(username=user_name, password=user_password)

        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, 'Successfully Logged in')
            return redirect('home')
        else:
            messages.error(request, 'There is no user check your username or password')
            return redirect('login')

    return render(request, 'login.html')

def user_registration(request):

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')
        user_conf_password = request.POST.get('user_conf_password')

        if user_password != user_conf_password:
            messages.error(request, 'Password is not matching...')
            return redirect('register')
        elif len(user_name) > 8 :
            messages.error(request,'Username should not more than 8 characters...')
            return redirect('register')
        else:
            user = User.objects.create_user(user_name, user_email, user_password)
            user.save()
            messages.error(request, 'Successfully registered')
            return redirect('login')

    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect('home')

