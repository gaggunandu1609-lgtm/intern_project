from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User


def register(request):

    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            role=request.POST['role']
        )
        return redirect('login')

    return render(request, 'register.html')


def user_login(request):

    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')